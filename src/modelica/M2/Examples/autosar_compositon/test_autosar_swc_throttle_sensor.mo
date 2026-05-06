within M2.Examples.autosar_compositon;
model test_autosar_swc_throttle_sensor
  annotation (__MWORKS(version = "2025a", ContinueSimConfig(SaveContinueFile = "false", SaveBeforeStop = "false", NumberBeforeStop = 1, FixedContinueInterval = "false", ContinueIntervalLength = 0.5, ContinueTimeVector)), experiment(Algorithm = Dassl, InlineIntegrator = false, InlineStepSize = false, Interval = 0.02, StartTime = 0, StopTime = 10, Tolerance = 0.0001));
  autosar_swc_throttle_sensor autosar_swc_throttle_sensor1
    annotation (Placement(transformation(origin = {-107, 20}, 
      extent = {{-27, -10}, {27, 10}})));
  Modelica.Blocks.Sources.Sine sine(f(displayUnit = "rad/s") = 0.159154943091895, amplitude = 1000)
    annotation (Placement(transformation(origin = {-196, 20}, 
      extent = {{-10, -10}, {10, 10}})));
equation 
  connect(sine.y, autosar_swc_throttle_sensor1.TPS_HwIO_Value_input)
    annotation (Line(origin = {-143, 20}, 
      points = {{-42, 0}, {41.4778, 0}, {41.4778, 0.2}}, 
      color = {0, 0, 127}));

end test_autosar_swc_throttle_sensor;