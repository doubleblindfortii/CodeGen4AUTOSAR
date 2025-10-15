function TraceInfoFlag() {
    this.traceFlag = new Array();
}
top.TraceInfoFlag.instance = new TraceInfoFlag();
function TraceInfoLineFlag() {
    this.lineTraceFlag = new Array();
    this.lineTraceFlag["autosar_swc_throttle_sensor.c:77"]=1;
    this.lineTraceFlag["autosar_swc_throttle_sensor.c:83"]=1;
    this.lineTraceFlag["autosar_swc_throttle_sensor.c:84"]=1;
    this.lineTraceFlag["autosar_swc_throttle_sensor.c:85"]=1;
    this.lineTraceFlag["autosar_swc_throttle_sensor.h:32"]=1;
    this.lineTraceFlag["autosar_swc_throttle_sensor.h:37"]=1;
}
top.TraceInfoLineFlag.instance = new TraceInfoLineFlag();
