within M2.Examples.autosar_compositon;
model test_autosar_swc_pedal_sensor
  annotation (__MWORKS(version = "2025a"));
  autosar_swc_pedal_sensor autosar_swc_pedal_sensor1(runnable_Step_sys(Setpoint_Lookup(extrapolation = Modelica.Blocks.Types.Extrapolation.HoldLastPoint)))
    annotation (Placement(transformation(origin = {-187, -2}, 
      extent = {{-33, -42}, {33, 42}})));
  Modelica.Blocks.Sources.Sine sine(f(displayUnit = "rad/s") = 0.159154943091895, amplitude = 1000)
    annotation (Placement(transformation(origin = {-330, 0}, extent = {{-10, -10}, {10, 10}})));
equation 
  connect(sine.y, autosar_swc_pedal_sensor1.APP_HwIO_Value_input)
    annotation (Line(origin = {-273, 0}, 
      points = {{-46, 0}, {46.4, 0}, {46.4, 0.52}}, 
      color = {0, 0, 127}));

end test_autosar_swc_pedal_sensor;