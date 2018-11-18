close all;

proj_dir = '/Users/yunjunz/insarlab/Galapagos/GalapagosSenDT128/PYSAR/GEOCODE/';
mask = h5read([proj_dir, 'maskVolcanoes1.h5'], '/mask');
ts = h5read([proj_dir, 'geo_timeseries_ECMWF_ramp_demErr.h5'], '/timeseries') * 100.0;

ts = ts - ts(:,:,10);
[~, ~, z] = size(ts);
mask = repmat(mask, 1, 1, z);
ts(mask==1) = nan;
clear mask;
ts = permute(ts, [3, 1, 2]);

% re-wrap into [w0, w1]
w0 = -15;
w1 = 15;
ts = w0 + mod(ts-w0, w1-w0);

ts = ts(:, 201:1500, 101:1850); %all volcanoes
%ts = ts(:, 201:650, 701:1100); %Fernandina
[y, x, z] = size(ts);
for i = 1:y
    ts(:,i,:) = flipud(ts(:,i,:));
end
[xx, yy, zz] = meshgrid(1:x, 1:y, 1:z);

xslice = 1;
yslice = y:-1:1;
zslice = 1; %1:20:z;

h = slice(xx,yy,zz,ts,xslice,yslice,zslice);
set(h, 'EdgeColor', 'none');
view(-135, 0);
daspect([10,1,10])
%axes('Units', 'normalized', 'Position', [0 0 1 1])
axis vis3d;
axis off;
colormap(jet(300));
%colorbar;
%box on;


