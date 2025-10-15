function TraceInfoFlag() {
    this.traceFlag = new Array();
}
top.TraceInfoFlag.instance = new TraceInfoFlag();
function TraceInfoLineFlag() {
    this.lineTraceFlag = new Array();
    this.lineTraceFlag["autosar_swc_pedal_sensor.c:77"]=1;
    this.lineTraceFlag["autosar_swc_pedal_sensor.c:79"]=1;
    this.lineTraceFlag["autosar_swc_pedal_sensor.c:80"]=1;
}
top.TraceInfoLineFlag.instance = new TraceInfoLineFlag();
