function export_autosar_signals(model, signal_names, dt, outfile)
% =========================================================
% AUTOSAR / Simulink 信号导出工具（带表头 + 多维支持）
%
% 用法：
% export_autosar_signals('model', {'sig1','sig2'}, 0.02, 'out.csv')
%
% 特性：
% ✔ 自动仿真
% ✔ 自动重采样（ZOH）
% ✔ 支持多维信号（自动展开）
% ✔ 自动生成列名
% ✔ 输出 CSV（带 header）
% =========================================================

%% ===== 1. 仿真 =====
open_system(model);

out = sim(model, ...
    'SaveFormat','Dataset', ...
    'SignalLogging','on');

logs = out.logsout;

%% ===== 2. 获取时间范围 =====
ts0 = logs.get(signal_names{1});
t_end = ts0.Values.Time(end);

time_new = 0:dt:t_end;
N = length(time_new);

%% ===== 3. 初始化 =====
data_all = time_new';
var_names = {'time'};

%% ===== 4. 遍历信号 =====
for i = 1:length(signal_names)

    name = signal_names{i};
    ts = logs.get(name);

    if isempty(ts)
        warning('⚠️ 信号不存在: %s', name);
        continue;
    end

    t = ts.Values.Time;
    d = double(ts.Values.Data);

    % ===== 插值（ZOH）=====
    d_new = interp1(t, d, time_new, 'previous','extrap');

    % ===== 强制统一形状 =====
    d_new = reshape(d_new, N, []);

    % ===== 拼接数据 =====
    data_all = [data_all, d_new];

    % ===== 自动生成列名 =====
    dim = size(d_new, 2);

    if dim == 1
        var_names{end+1} = name;
    else
        for k = 1:dim
            var_names{end+1} = sprintf('%s_%d', name, k);
        end
    end
end

%% ===== 5. 导出 =====
T = array2table(data_all, 'VariableNames', var_names);
writetable(T, outfile);

fprintf('✅ 导出完成: %s\n', outfile);

end