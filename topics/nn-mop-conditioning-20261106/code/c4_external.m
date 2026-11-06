function c4_external(src,input_file,out_file,mode)
  % Local headless wrapper; third-party functions are unchanged.
  addpath(fullfile(src,'algorithms')); addpath(fullfile(src,'utils'));
  data=jsondecode(fileread(input_file)); out={};
  for idx=1:numel(data)
    c=data(idx); n=c.N;
    if strcmp(mode,'m2') && ~(n==6 && strcmp(c.family,'krawtchouk')), continue; end
    for kind=1:2
      if kind==1
        if strcmp(c.family,'krawtchouk')
          [Z,v1,w1,w2,l1,l2]=kravchuk_data(n-1,0.4,0.5);
          exact=kravchuk_exact(n-1,0.4,0.5);
        else
          [Z,v1,w1,w2,l1,l2]=hahn_data(n-1,1,1.5,1);
          exact=hahn_exact(n-1,1,1.5,1);
        end
        label='archive_integer';
      else
        Z=diag(hex2num(reshape(c.nodes_bits,16,[])'));
        l1=hex2num(reshape(c.weights_bits{1},16,[])');
        l2=hex2num(reshape(c.weights_bits{2},16,[])');
        v1=ones(n,1); [w1,w2]=IEP_initial_data(diag(Z),l1,l2);
        exact=[]; label='shared_normalized';
      end
      r=struct('N',n,'family',c.family,'input_kind',label,'nodes',diag(Z)',...
          'weights',[l1';l2'],'exact',exact,'algorithms',struct());
      r.nodes_bits=reshape(num2hex(diag(Z)).',1,[]);
      r.weights1_bits=reshape(num2hex(l1).',1,[]);
      r.weights2_bits=reshape(num2hex(l2).',1,[]);
      r.exact_bits=reshape(num2hex(exact(:)).',1,[]);
      names={'CORE','KRYL','REORTH'};
      for k=1:3
        try
          if k==1, [H,V,W]=IEP_CORE(Z,v1,w1,w2);
          elseif k==2, [H,V,W]=IEP_KRYL(Z,v1,w1,w2);
          else, [H,V,W]=IEP_KRYLREORTH(Z,v1,w1,w2,'full',1); end
          r.algorithms.(names{k})=struct('H',H,'H_bits',reshape(num2hex(H(:)).',1,[]),'bior',norm(W'*V-eye(n)),'status','ok');
        catch err
          r.algorithms.(names{k})=struct('status','error','message',err.message);
        end
      end
      out{end+1}=r;
    end
  end
  fid=fopen(out_file,'w'); fprintf(fid,'%s',jsonencode(out)); fclose(fid);
end
