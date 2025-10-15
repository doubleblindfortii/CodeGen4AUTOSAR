function RTW_rtwnameSIDMap() {
	this.rtwnameHashMap = new Array();
	this.sidHashMap = new Array();
	this.rtwnameHashMap["<Root>"] = {sid: "autosar_swc_pedal_sensor"};
	this.sidHashMap["autosar_swc_pedal_sensor"] = {rtwname: "<Root>"};
	this.rtwnameHashMap["<S1>"] = {sid: "autosar_swc_pedal_sensor:3"};
	this.sidHashMap["autosar_swc_pedal_sensor:3"] = {rtwname: "<S1>"};
	this.rtwnameHashMap["<Root>/APP_HwIO_Value"] = {sid: "autosar_swc_pedal_sensor:4"};
	this.sidHashMap["autosar_swc_pedal_sensor:4"] = {rtwname: "<Root>/APP_HwIO_Value"};
	this.rtwnameHashMap["<Root>/Runnable_Step_sys"] = {sid: "autosar_swc_pedal_sensor:3"};
	this.sidHashMap["autosar_swc_pedal_sensor:3"] = {rtwname: "<Root>/Runnable_Step_sys"};
	this.rtwnameHashMap["<Root>/APP_Percent_Value"] = {sid: "autosar_swc_pedal_sensor:6"};
	this.sidHashMap["autosar_swc_pedal_sensor:6"] = {rtwname: "<Root>/APP_Percent_Value"};
	this.rtwnameHashMap["<S1>/APP_HwIO_Value_read"] = {sid: "autosar_swc_pedal_sensor:5"};
	this.sidHashMap["autosar_swc_pedal_sensor:5"] = {rtwname: "<S1>/APP_HwIO_Value_read"};
	this.rtwnameHashMap["<S1>/Data Type Conversion2"] = {sid: "autosar_swc_pedal_sensor:14"};
	this.sidHashMap["autosar_swc_pedal_sensor:14"] = {rtwname: "<S1>/Data Type Conversion2"};
	this.rtwnameHashMap["<S1>/Setpoint Lookup"] = {sid: "autosar_swc_pedal_sensor:12"};
	this.sidHashMap["autosar_swc_pedal_sensor:12"] = {rtwname: "<S1>/Setpoint Lookup"};
	this.rtwnameHashMap["<S1>/APP_Percent_Value_write"] = {sid: "autosar_swc_pedal_sensor:7"};
	this.sidHashMap["autosar_swc_pedal_sensor:7"] = {rtwname: "<S1>/APP_Percent_Value_write"};
	this.getSID = function(rtwname) { return this.rtwnameHashMap[rtwname];}
	this.getRtwname = function(sid) { return this.sidHashMap[sid];}
}
RTW_rtwnameSIDMap.instance = new RTW_rtwnameSIDMap();
