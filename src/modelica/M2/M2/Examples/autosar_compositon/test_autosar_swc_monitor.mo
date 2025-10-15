model test_autosar_swc_monitor
  annotation(__MWORKS(version="2025a"));
  autosar_swc_monitor autosar_swc_monitor1 
    annotation (Placement(transformation(origin={-132,24}, 
extent={{-28,-24},{28,24}})));
  Modelica.Blocks.Sources.Sine sine(f(displayUnit="rad/s")=0.159154943091895) 
    annotation (Placement(transformation(origin = {-260, 40}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Sources.Sine sine1(f(displayUnit="rad/s")=0.159154943091895) 
    annotation (Placement(transformation(origin = {-260, -10}, extent = {{-10, -10}, {10, 10}})));
equation
  connect(sine.y, autosar_swc_monitor1.TPS_Seconday_Value_input) 
  annotation(Line(origin={-207,35}, 
  points={{-42,5},{41.3992,5},{41.3992,-4.51604}}, 
  color={0,0,127}));
  connect(sine1.y, autosar_swc_monitor1.TPS_Primary_Value_input) 
  annotation(Line(origin={-207,5}, 
  points={{-42,-15},{41.3992,-15},{41.3992,14.2}}, 
  color={0,0,127}));

end test_autosar_swc_monitor;