function CodeMetrics() {
	 this.metricsArray = {};
	 this.metricsArray.var = new Array();
	 this.metricsArray.fcn = new Array();
	 this.metricsArray.var["rtDW"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\autosar_swc.c",
	size: 8};
	 this.metricsArray.fcn["Rte_IRead_ASWC_Runnable_1s_ReceivePort_In1"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\stub\\Rte_ASWC.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Rte_IRead_ASWC_Runnable_2s_ReceivePort_In2"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\stub\\Rte_ASWC.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Rte_IWrite_ASWC_Runnable_1s_SenderPort_Out1"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\stub\\Rte_ASWC.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Rte_IWrite_ASWC_Runnable_1s_SenderPort_Out2"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\stub\\Rte_ASWC.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Rte_IrvIRead_ASWC_Runnable_1s_IRV1"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\stub\\Rte_ASWC.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Rte_IrvIWrite_ASWC_Runnable_2s_IRV1"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\stub\\Rte_ASWC.h",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Runnable_1s"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\autosar_swc.c",
	stack: 16,
	stackTotal: 16};
	 this.metricsArray.fcn["Runnable_2s"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\autosar_swc.c",
	stack: 0,
	stackTotal: 0};
	 this.metricsArray.fcn["Runnable_Initialize"] = {file: "I:\\学习\\科研\\论文\\实验&进展\\autosar\\autosar_swc_autosar_rtw\\autosar_swc.c",
	stack: 0,
	stackTotal: 0};
	 this.getMetrics = function(token) { 
		 var data;
		 data = this.metricsArray.var[token];
		 if (!data) {
			 data = this.metricsArray.fcn[token];
			 if (data) data.type = "fcn";
		 } else { 
			 data.type = "var";
		 }
	 return data; }; 
	 this.codeMetricsSummary = '<a href="autosar_swc_metrics.html">Global Memory: 8(bytes) Maximum Stack: 16(bytes)</a>';
	}
CodeMetrics.instance = new CodeMetrics();
