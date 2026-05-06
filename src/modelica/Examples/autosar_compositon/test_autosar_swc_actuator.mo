within M2.Examples.autosar_compositon;
model test_autosar_swc_actuator
  annotation (__MWORKS(version = "2025a"));
  autosar_swc_actuator autosar_swc_actuator1(runnable_Step_sys(HBridgeDriverLookup(extrapolation = Modelica.Blocks.Types.Extrapolation.HoldLastPoint, smoothness = Modelica.Blocks.Types.Smoothness.ConstantSegments)))
    annotation (Placement(transformation(origin = {-54, 13}, 
      extent = {{-36, -27}, {36, 27}})));
  Modelica.Blocks.Sources.Sine sine(f(displayUnit = "rad/s") = 0.159154943091895, amplitude = 100)
    annotation (Placement(transformation(origin = {-180, 20}, extent = {{-10, -10}, {10, 10}})));
equation 
  connect(sine.y, autosar_swc_actuator1.ThrCmd_Percent_Value_input)
    annotation (Line(origin = {-132, 17}, 
      points = {{-37, 3}, {37.38, 3}, {37.38, -3.685}}, 
      color = {0, 0, 127}));

end test_autosar_swc_actuator;