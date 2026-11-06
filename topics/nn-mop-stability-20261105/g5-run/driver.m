% Headless replica of experiment_Hahn_Kravchuk.m loop (no plotting). Usage: octave --no-gui --eval "driver('<codeSrc>','<outdir>')"
function driver(src,outdir)
  addpath(fullfile(src,'algorithms')); addpath(fullfile(src,'utils'));
  N = 5:30;
  fams = {'kravchuk','hahn'};
  for f = 1:2
    E = zeros(numel(N),8); t0=tic;
    for idx = 1:numel(N)
      m = N(idx);
      if f==2
        [Z,v1,w1,w2] = hahn_data(m,1,1.5,1); H = hahn_exact(m,1,1.5,1);
      else
        [Z,v1,w1,w2] = kravchuk_data(m,0.4,0.5); H = kravchuk_exact(m,0.4,0.5);
      end
      [Hc,Vc,Wc] = IEP_CORE(Z,v1,w1,w2);
      [Hk,Vk,Wk] = IEP_KRYL(Z,v1,w1,w2);
      [Hr,Vr,Wr] = IEP_KRYLREORTH(Z,v1,w1,w2,'full',1);
      E(idx,:) = [m, norm(H-Hc)/norm(H), norm(H-Hk)/norm(H), norm(H-Hr)/norm(H), ...
        norm(Wc'*Vc-eye(size(Wc,1))), norm(Wk'*Vk-eye(size(Wk,1))), norm(Wr'*Vr-eye(size(Wr,1))), NaN];
    end
    fprintf('%s done in %.2f s\n',fams{f},toc(t0));
    fid=fopen(fullfile(outdir,['ours_' fams{f} '.dat']),'w');
    for i=1:size(E,1), fprintf(fid,'%d %.15e %.15e %.15e %.15e %.15e %.15e\n',E(i,1:7)); end
    fclose(fid);
  end
end
