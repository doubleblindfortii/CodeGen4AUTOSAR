within M2.Examples.autosar_compositon;
model autosar_swc_controller
  annotation (Icon(coordinateSystem(extent = {{-100, -100}, {100, 100}}, 
    grid = {2, 2}), graphics = {Rectangle(origin = {0, 0}, 
    fillColor = {255, 255, 255}, 
    fillPattern = FillPattern.Solid, 
    extent = {{-100, 100}, {100, -100}}), Text(origin = {0, 84}, 
    lineColor = {0, 0, 0}, 
    extent = {{-74, 10}, {74, -10}}, 
    textString = "autosar_swc_controller", 
    textStyle = {TextStyle.None}, 
    textColor = {0, 0, 0}, 
    horizontalAlignment = LinePattern.None), Text(origin = {2.21563, -115.656}, 
    lineColor = {0, 0, 0}, 
    extent = {{-46.9713, 11.2997}, {46.9713, -11.2997}}, 
    textString = "%name", 
    textStyle = {TextStyle.None}, 
    textColor = {0, 0, 0}, 
    horizontalAlignment = LinePattern.None)}));


  model RunnableEntity_Step_sys_controller
    //extends M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity;
    Modelica.Blocks.Interfaces.RealInput APP_Percent_Value_read 
      annotation (Placement(transformation(origin = {-112.42967700958253, 51.179707527160645}, 
        extent = {{-11.249969482421875, -11.249969482421871}, {11.24996948242189, 11.249969482421868}})));
    Modelica.Blocks.Interfaces.RealInput TPS_Percent_Value_read 
      annotation (Placement(transformation(origin = {-111.99999999999997, -44.82029247283936}, 
        extent = {{-10.820292472839355, -10.820292472839355}, {10.820292472839327, 10.820292472839363}})));
    Modelica.Blocks.Interfaces.RealOutput ThrCmd_Percent_Value_write 
      annotation (Placement(transformation(origin = {108.194, 1.03226}, 
        extent = {{-10, -10}, {10, 10}})));
    Modelica.Blocks.Math.Add add(k2 = -1) 
      annotation (Placement(transformation(extent = {{-10.0, -10.0}, {10.0, 10.0}})));
    Modelica.Blocks.Continuous.PID PID1 
      annotation (Placement(transformation(origin={58,0}, 
extent={{-10,-10},{10,10}})));
    annotation();
  equation
    connect(add.u1, APP_Percent_Value_read) 
      annotation (Line(origin = {-206.0, 28.0}, 
        points = {{194.0, -22.0}, {170.0, -22.0}, {170.0, 23.0}, {94.0, 23.0}}, 
        color = {0, 0, 127}));
    connect(add.u2, TPS_Percent_Value_read) 
      annotation (Line(origin = {-206.0, -10.0}, 
        points = {{194.0, 4.0}, {170.0, 4.0}, {170.0, -35.0}, {94.0, -35.0}}, 
        color = {0, 0, 127}));
    connect(add.y, PID1.u) 
      annotation (Line(origin={26,1}, 
points={{-15,-1},{20,-1}}, 
color={0,0,127}));
    connect(PID1.y, ThrCmd_Percent_Value_write) 
      annotation (Line(origin={87,1}, 
points={{-18,-1},{21.194,-1},{21.194,0.03226}}, 
color={0,0,127}));
    end RunnableEntity_Step_sys_controller;


  VisibleElements.RPORT TPS_Percent_Value(filter = false) 
    annotation (Placement(transformation(origin = {-55.4372, -14.4236}, 
      extent = {{-10, -10}, {10, 10}})));
  VisibleElements.RPORT APP_Percent_Value(filter = false) 
    annotation (Placement(transformation(origin = {-54.593, 35.9985}, 
      extent = {{-10, -10}, {10, 10}})));
  VisibleElements.PPORT ThrCmd_Percent_Value 
    annotation (Placement(transformation(origin = {116.66664123535153, 0.0}, 
      extent = {{-16.66664123535155, -16.666641235351545}, {16.666641235351562, 16.66664123535155}})));
  RunnableEntity_Step_sys_controller runnable_Step_sys 
    annotation (Placement(transformation(origin = {25.999999999999993, 8.881784197001252e-16}, 
      extent = {{-30.0, -16.66668362098507}, {30.0, 16.66668362098507}})));
  Modelica.Blocks.Interfaces.RealInput TPS_Percent_Value_input 
    annotation (Placement(transformation(origin = {-119.437, -14.7236}, 
      extent = {{-20, -20}, {20, 20}})));
  Modelica.Blocks.Interfaces.RealInput APP_Percent_Value_input 
    annotation (Placement(transformation(origin = {-118.593, 35.6985}, 
      extent = {{-20, -20}, {20, 20}})));
equation
  connect(TPS_Percent_Value_input, TPS_Percent_Value.u) 
    annotation (Line(origin = {-312.437, -14.7236}, 
      points = {{193, 0}, {246.75, 0}, {246.75, 1.42109e-14}}, 
      color = {0, 0, 127}));
  connect(APP_Percent_Value_input, APP_Percent_Value.u) 
    annotation (Line(origin = {-306.593, 65.6985}, 
      points = {{188, -30}, {241.75, -30}}, 
      color = {0, 0, 127}));
  connect(runnable_Step_sys.ThrCmd_Percent_Value_write, ThrCmd_Percent_Value) 
    annotation (Line(origin = {88.0, 0.0}, 
      points = {{-29.0, 0.0}, {29.0, 0.0}}, 
      color = {0, 0, 127}));
  connect(runnable_Step_sys.APP_Percent_Value_read, APP_Percent_Value.y_) 
    annotation (Line(origin = {-26, 22}, 
      points = {{18.2711, -13.47}, {-18.543, -13.47}, {-18.543, 13.5985}}, 
      color = {0, 0, 127}));
  connect(runnable_Step_sys.TPS_Percent_Value_read, TPS_Percent_Value.y_) 
    annotation (Line(origin = {-26, -11}, 
      points = {{18.4, 3.52994}, {-19.3872, 3.52994}, {-19.3872, -3.82362}}, 
      color = {0, 0, 127}));
end autosar_swc_controller;