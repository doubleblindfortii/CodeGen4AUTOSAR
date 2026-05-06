within M2.Examples;
model AUTOSAR_HeadLamp
  HeadLamp headlamp_left
    annotation (Placement(transformation(origin = {-28, 88.713}, 
      extent = {{-19.5147, -14.713}, {19.5147, 14.713}})));
  M2.Examples.Swc_Expfcns_Example.Swc_Expfcns SWC
    annotation (Placement(transformation(origin = {-99.0473, 18.7289}, 
      extent = {{-14.3623, -16.7092}, {14.3623, 16.7092}})));
  HeadLamp headlamp_right
    annotation (Placement(transformation(origin = {0.9415, -12.147}, 
      extent = {{-19.0585, -15.853}, {19.0585, 15.853}})));
  Modelica.Blocks.Sources.Constant const(k = 0)
    annotation (Placement(transformation(origin = {-140.498, 28.2138}, 
      extent = {{-10, -10}, {10, 10}})));
  annotation (__MWORKS);
equation 
  connect(SWC.PPort_1, headlamp_left.switch)
    annotation (Line(origin = {-78, 48}, 
      points = {{-7.84099, -17.8373}, {2.2188, -17.8373}, {2.2188, 46.8521}, {26.6743, 46.8521}}, 
      color = {0, 0, 127}), __MWORKS(BlockSystem(NamedSignal)));
  connect(SWC.PPort_3, headlamp_right.switch)
    annotation (Line(origin = {-70, -18}, 
      points = {{-0.614111, 44.0611}, {48.1611, 44.0611}, {48.1611, 12.4677}}, 
      color = {0, 0, 127}));
  connect(headlamp_right.voltageInput, SWC.PPort_4)
    annotation (Line(origin = {-70, -34}, 
      points = {{48.0416, 14.4425}, {-2.28284, 14.4425}, {-2.28284, 55.3532}, {-0.717089, 55.3532}}, 
      color = {0, 0, 127}), __MWORKS(BlockSystem(NamedSignal)));
  connect(const.y, SWC.u1)
    annotation (Line(origin = {-174.646, 26.7099}, 
      points = {{45.1479, 1.50383}, {59.6775, 1.50383}, {59.6775, 2.66503}}, 
      color = {0, 0, 127}));
  connect(const.y, SWC.u)
    annotation (Line(origin = {-177.646, 16.7099}, 
      points = {{48.1479, 11.5038}, {53.0257, 11.5038}, {53.0257, 2.29503}, {62.7483, 2.29503}}, 
      color = {0, 0, 127}), __MWORKS(BlockSystem(NamedSignal)));
  connect(SWC.u2, const.y)
    annotation (Line(origin = {-177.646, 8.70992}, 
      points = {{62.7144, 0.0837911}, {53.2776, 0.0837911}, {53.2776, 19.5038}, {48.1479, 19.5038}}, 
      color = {0, 0, 127}), __MWORKS(BlockSystem(NamedSignal)));
  connect(SWC.PPort_4, headlamp_left.voltageInput)
    annotation (Line(origin = {-62, 18}, 
      points = {{-8.71709, 3.3532}, {-8.71709, -2.40973}, {-2, -2.40973}, {-2, 63.8354}, {10.5519, 63.8354}}, 
      color = {0, 0, 127}), __MWORKS(BlockSystem(NamedSignal)));
end AUTOSAR_HeadLamp;