function RTW_rtwnameSIDMap() {
	this.rtwnameHashMap = new Array();
	this.sidHashMap = new Array();
	this.rtwnameHashMap["<Root>"] = {sid: "autosar_swc_throttle_sensor"};
	this.sidHashMap["autosar_swc_throttle_sensor"] = {rtwname: "<Root>"};
	this.rtwnameHashMap["<S1>"] = {sid: "autosar_swc_throttle_sensor:3"};
	this.sidHashMap["autosar_swc_throttle_sensor:3"] = {rtwname: "<S1>"};
	this.rtwnameHashMap["<Root>/TPS_HwIO_Value"] = {sid: "autosar_swc_throttle_sensor:4"};
	this.sidHashMap["autosar_swc_throttle_sensor:4"] = {rtwname: "<Root>/TPS_HwIO_Value"};
	this.rtwnameHashMap["<Root>/Runnable_Step_sys"] = {sid: "autosar_swc_throttle_sensor:3"};
	this.sidHashMap["autosar_swc_throttle_sensor:3"] = {rtwname: "<Root>/Runnable_Step_sys"};
	this.rtwnameHashMap["<Root>/TPS_Percent_Value"] = {sid: "autosar_swc_throttle_sensor:6"};
	this.sidHashMap["autosar_swc_throttle_sensor:6"] = {rtwname: "<Root>/TPS_Percent_Value"};
	this.rtwnameHashMap["<S1>/TPS_HwIO_Value_read"] = {sid: "autosar_swc_throttle_sensor:5"};
	this.sidHashMap["autosar_swc_throttle_sensor:5"] = {rtwname: "<S1>/TPS_HwIO_Value_read"};
	this.rtwnameHashMap["<S1>/Data Type Conversion"] = {sid: "autosar_swc_throttle_sensor:11"};
	this.sidHashMap["autosar_swc_throttle_sensor:11"] = {rtwname: "<S1>/Data Type Conversion"};
	this.rtwnameHashMap["<S1>/TPS Lookup"] = {sid: "autosar_swc_throttle_sensor:19"};
	this.sidHashMap["autosar_swc_throttle_sensor:19"] = {rtwname: "<S1>/TPS Lookup"};
	this.rtwnameHashMap["<S1>/TPS_Percent_Value_write"] = {sid: "autosar_swc_throttle_sensor:7"};
	this.sidHashMap["autosar_swc_throttle_sensor:7"] = {rtwname: "<S1>/TPS_Percent_Value_write"};
	this.getSID = function(rtwname) { return this.rtwnameHashMap[rtwname];}
	this.getRtwname = function(sid) { return this.sidHashMap[sid];}
}
RTW_rtwnameSIDMap.instance = new RTW_rtwnameSIDMap();
