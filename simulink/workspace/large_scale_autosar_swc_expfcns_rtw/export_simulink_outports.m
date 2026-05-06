function export_simulink_outports(model, dt, outfile)

open_system(model)

% 仿真
out = sim(model, ...
    'SaveFormat','Dataset', ...
    'SignalLogging','on');

logs = out.logsout;

% === 自动获取所有信号名字 ===
names = logs.getElementNames;

% === 时间轴 ===
ts0 = logs.get(names{1});
time_new = 0:dt:ts0.Values.Time(end);
N = length(time_new);

data_all = time_new';
var_names = {'time'};

% === 遍历所有信号 ===
for i = 1:length(names)

    ts = logs.get(names{i});

    d_new = interp1(ts.Values.Time, double(ts.Values.Data), ...
                    time_new, 'previous','extrap');

    % 统一形状
    d_new = reshape(d_new, N, []);

    % 拼接
    data_all = [data_all, d_new];

    % ===== 自动列名 =====
    dim = size(d_new,2);

    if dim == 1
        var_names{end+1} = names{i};
    else
        for k = 1:dim
            var_names{end+1} = sprintf('%s_%d', names{i}, k);
        end
    end
end

% === 导出 ===
T = array2table(data_all, 'VariableNames', var_names);
writetable(T, outfile);

fprintf('✅ export complete: %s\n', outfile);

end