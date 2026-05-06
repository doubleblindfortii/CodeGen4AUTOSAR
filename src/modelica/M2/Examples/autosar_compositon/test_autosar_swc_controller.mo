within M2.Examples.autosar_compositon;
model test_autosar_swc_controller
  annotation (__MWORKS(version = "2025a"));
  autosar_swc_controller autosar_swc_controller1(runnable_Step_sys(PID1(Td = 0)))
    annotation (Placement(transformation(origin = {-90, 22}, 
      extent = {{-40, -28}, {40, 28}})));
  Modelica.Blocks.Sources.Sine sine(f(displayUnit = "rad/s") = 0.159154943091895)
    annotation (Placement(transformation(origin = {-238, 4}, 
      extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Sources.Constant const(k = 0)
    annotation (Placement(transformation(origin = {-238, 74}, 
      extent = {{-10, -10}, {10, 10}})));
equation 
  connect(const.y, autosar_swc_controller1.APP_Percent_Value_input)
    annotation (Line(origin = {-178, 11}, 
      points = {{-49, 63}, {40.5628, 63}, {40.5628, 20.9956}}, 
      color = {0, 0, 127}));
  connect(sine.y, autosar_swc_controller1.TPS_Percent_Value_input)
    annotation (Line(origin = {-182, 11}, 
      points = {{-45, -7}, {44.2252, -7}, {44.2252, 6.87739}}, 
      color = {0, 0, 127}));

end test_autosar_swc_controller;