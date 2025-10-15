function TraceInfoFlag() {
    this.traceFlag = new Array();
}
top.TraceInfoFlag.instance = new TraceInfoFlag();
function TraceInfoLineFlag() {
    this.lineTraceFlag = new Array();
    this.lineTraceFlag["autosar_swc_monitor.c:29"]=1;
    this.lineTraceFlag["autosar_swc_monitor.c:30"]=1;
    this.lineTraceFlag["autosar_swc_monitor.c:32"]=1;
    this.lineTraceFlag["autosar_swc_monitor.c:39"]=1;
    this.lineTraceFlag["autosar_swc_monitor.h:30"]=1;
}
top.TraceInfoLineFlag.instance = new TraceInfoLineFlag();
