function RTW_rtwnameSIDMap() {
	this.rtwnameHashMap = new Array();
	this.sidHashMap = new Array();
	this.rtwnameHashMap["<Root>"] = {sid: "autosar_swc_actuator"};
	this.sidHashMap["autosar_swc_actuator"] = {rtwname: "<Root>"};
	this.rtwnameHashMap["<S1>"] = {sid: "autosar_swc_actuator:3"};
	this.sidHashMap["autosar_swc_actuator:3"] = {rtwname: "<S1>"};
	this.rtwnameHashMap["<Root>/ThrCmd_Percent_Value"] = {sid: "autosar_swc_actuator:4"};
	this.sidHashMap["autosar_swc_actuator:4"] = {rtwname: "<Root>/ThrCmd_Percent_Value"};
	this.rtwnameHashMap["<Root>/Runnable_Step_sys"] = {sid: "autosar_swc_actuator:3"};
	this.sidHashMap["autosar_swc_actuator:3"] = {rtwname: "<Root>/Runnable_Step_sys"};
	this.rtwnameHashMap["<Root>/ThrCmd_HwIO_Value"] = {sid: "autosar_swc_actuator:6"};
	this.sidHashMap["autosar_swc_actuator:6"] = {rtwname: "<Root>/ThrCmd_HwIO_Value"};
	this.rtwnameHashMap["<S1>/ThrCmd_Percent_Value_read"] = {sid: "autosar_swc_actuator:5"};
	this.sidHashMap["autosar_swc_actuator:5"] = {rtwname: "<S1>/ThrCmd_Percent_Value_read"};
	this.rtwnameHashMap["<S1>/Data Type Conversion"] = {sid: "autosar_swc_actuator:11"};
	this.sidHashMap["autosar_swc_actuator:11"] = {rtwname: "<S1>/Data Type Conversion"};
	this.rtwnameHashMap["<S1>/HBridgeDriver Lookup"] = {sid: "autosar_swc_actuator:12"};
	this.sidHashMap["autosar_swc_actuator:12"] = {rtwname: "<S1>/HBridgeDriver Lookup"};
	this.rtwnameHashMap["<S1>/Scope"] = {sid: "autosar_swc_actuator:18"};
	this.sidHashMap["autosar_swc_actuator:18"] = {rtwname: "<S1>/Scope"};
	this.rtwnameHashMap["<S1>/ThrCmd_HwIO_Value_write"] = {sid: "autosar_swc_actuator:7"};
	this.sidHashMap["autosar_swc_actuator:7"] = {rtwname: "<S1>/ThrCmd_HwIO_Value_write"};
	this.getSID = function(rtwname) { return this.rtwnameHashMap[rtwname];}
	this.getRtwname = function(sid) { return this.sidHashMap[sid];}
}
RTW_rtwnameSIDMap.instance = new RTW_rtwnameSIDMap();
