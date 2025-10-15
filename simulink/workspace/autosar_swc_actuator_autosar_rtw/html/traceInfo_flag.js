function TraceInfoFlag() {
    this.traceFlag = new Array();
}
top.TraceInfoFlag.instance = new TraceInfoFlag();
function TraceInfoLineFlag() {
    this.lineTraceFlag = new Array();
    this.lineTraceFlag["autosar_swc_actuator.c:69"]=1;
    this.lineTraceFlag["autosar_swc_actuator.c:70"]=1;
}
top.TraceInfoLineFlag.instance = new TraceInfoLineFlag();
