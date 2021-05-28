import pytest


from scenariogeneration import xosc as OSC
from scenariogeneration import prettyprint
from scenariogeneration.xosc.exceptions import NoActionsDefinedError

TD = OSC.TransitionDynamics(OSC.DynamicsShapes.step,OSC.DynamicsDimension.rate,1)


def test_speedaction_abs():
    speedaction = OSC.AbsoluteSpeedAction(50,TD)
    prettyprint(speedaction.get_element())

    speedaction2 = OSC.AbsoluteSpeedAction(50,TD)
    speedaction3 = OSC.AbsoluteSpeedAction(51,TD)
    assert speedaction == speedaction2
    assert speedaction != speedaction3

def test_speedaction_rel():
    speedaction = OSC.RelativeSpeedAction(1,'Ego',TD)

    prettyprint(speedaction.get_element())
    speedaction2 = OSC.RelativeSpeedAction(1,'Ego',TD)
    speedaction3 = OSC.RelativeSpeedAction(1,'Ego1',TD)
    assert speedaction == speedaction2
    assert speedaction != speedaction3

def test_longdistaction_dist():
    longdist = OSC.LongitudinalDistanceAction(1,'Ego')
    prettyprint(longdist.get_element())
    longdist2 = OSC.LongitudinalDistanceAction(1,'Ego')
    longdist3 = OSC.LongitudinalDistanceAction(2,'Ego')
    assert longdist == longdist2
    assert longdist != longdist3

def test_longdistaction_time():
    longdist = OSC.LongitudinalTimegapAction(2,'Ego',max_acceleration=1)
    prettyprint(longdist.get_element())
    longdist2 = OSC.LongitudinalTimegapAction(2,'Ego',max_acceleration=1)
    longdist3 = OSC.LongitudinalTimegapAction(3,'Ego',max_acceleration=1)
    assert longdist == longdist2
    assert longdist != longdist3

def test_lanechange_abs():
    lanechange = OSC.AbsoluteLaneChangeAction(1,TD)
    prettyprint(lanechange.get_element())
    lanechange2 = OSC.AbsoluteLaneChangeAction(1,TD)
    lanechange3 = OSC.AbsoluteLaneChangeAction(2,TD)
    assert lanechange == lanechange2
    assert lanechange != lanechange3

def test_lanechange_rel():
    lanechange = OSC.RelativeLaneChangeAction(1,'Ego',TD,0.2)
    prettyprint(lanechange.get_element())
    lanechange2 = OSC.RelativeLaneChangeAction(1,'Ego',TD,0.2)
    lanechange3 = OSC.RelativeLaneChangeAction(1,'Ego',TD,0.1)
    assert lanechange == lanechange2
    assert lanechange != lanechange3
    
def test_laneoffset_abs():
    laneoffset = OSC.AbsoluteLaneOffsetAction(1,OSC.DynamicsShapes.step,3,False)
    prettyprint(laneoffset.get_element())
    laneoffset2 = OSC.AbsoluteLaneOffsetAction(1,OSC.DynamicsShapes.step,3,False)
    laneoffset3 = OSC.AbsoluteLaneOffsetAction(1,OSC.DynamicsShapes.step,2,True)

    assert laneoffset == laneoffset2
    assert laneoffset != laneoffset3

def test_laneoffset_rel():
    laneoffset = OSC.RelativeLaneOffsetAction(1,'Ego',OSC.DynamicsShapes.step,3,False)
    prettyprint(laneoffset.get_element())
    laneoffset2 = OSC.RelativeLaneOffsetAction(1,'Ego',OSC.DynamicsShapes.step,3,False)
    laneoffset3 = OSC.RelativeLaneOffsetAction(1,'Ego',OSC.DynamicsShapes.linear,3,False)
    assert laneoffset == laneoffset2
    assert laneoffset != laneoffset3

def test_lateraldistance_noconst():
    latdist = OSC.LateralDistanceAction('Ego')
    prettyprint(latdist.get_element())
    latdist2 = OSC.LateralDistanceAction('Ego')
    latdist3 = OSC.LateralDistanceAction('Ego1')
    assert latdist == latdist2
    assert latdist != latdist3

def test_lateraldistance_const():
    latdist = OSC.LateralDistanceAction('Ego',3,max_speed=50)
    prettyprint(latdist.get_element())
    latdist2 = OSC.LateralDistanceAction('Ego',3,max_speed=50)
    latdist3 = OSC.LateralDistanceAction('Ego',3,max_speed=40)
    assert latdist == latdist2
    assert latdist != latdist3

def test_teleport():
    teleport = OSC.TeleportAction(OSC.WorldPosition())
    prettyprint(teleport.get_element())
    teleport2 = OSC.TeleportAction(OSC.WorldPosition())
    teleport3 = OSC.TeleportAction(OSC.WorldPosition(1))
    assert teleport == teleport2
    assert teleport != teleport3

def test_assign_route():
    
    route = OSC.Route('myroute')
    route.add_waypoint(OSC.WorldPosition(0,0,0,0,0,0),OSC.RouteStrategy.shortest)
    route.add_waypoint(OSC.WorldPosition(1,1,0,0,0,0),OSC.RouteStrategy.shortest)
    ara = OSC.AssignRouteAction(route)
    prettyprint(ara)
    ara2 = OSC.AssignRouteAction(route)
    route2 = OSC.Route('myroute2')
    route2.add_waypoint(OSC.WorldPosition(0,0,0,0,0,0),OSC.RouteStrategy.shortest)
    route2.add_waypoint(OSC.WorldPosition(1,1,1,0,0,0),OSC.RouteStrategy.shortest)
    ara3 = OSC.AssignRouteAction(route2)
    assert ara == ara2
    assert ara != ara3

def test_aqcuire_position_route():
    ara = OSC.AcquirePositionAction(OSC.WorldPosition(1,1,0,0,0,0))
    prettyprint(ara.get_element())
    ara2 = OSC.AcquirePositionAction(OSC.WorldPosition(1,1,0,0,0,0))
    ara3 = OSC.AcquirePositionAction(OSC.WorldPosition(1,1,1,0,0,0))
    assert ara == ara2
    assert ara != ara3

def test_activate_controller_action():
    aca = OSC.ActivateControllerAction(True,True)
    prettyprint(aca.get_element())
    aca2 = OSC.ActivateControllerAction(True,True)
    aca3 = OSC.ActivateControllerAction(True,False)
    assert aca == aca2
    assert aca != aca3

def test_assign_controller_action():
    prop = OSC.Properties()
    prop.add_property('mything','2')
    prop.add_property('theotherthing','true')

    cnt = OSC.Controller('mycontroller',prop)
    
    
    aca = OSC.AssignControllerAction(cnt)
    prettyprint(aca.get_element())

    prop2 = OSC.Properties()
    prop2.add_property('mything','3')
    prop2.add_property('theotherthing','true')

    cnt2 = OSC.Controller('mycontroller',prop2)
    
    
    aca2 = OSC.AssignControllerAction(cnt)
    aca3 = OSC.AssignControllerAction(cnt2)
    assert aca == aca2
    assert aca != aca3

def test_override_controller():
    ocva = OSC.OverrideControllerValueAction()
    with pytest.raises(NoActionsDefinedError):
        ocva.get_element()
    ocva.set_brake(True,2)
    prettyprint(ocva.get_element())
    ocva.set_throttle(False,0)
    prettyprint(ocva.get_element())
    ocva.set_clutch(True,1)
    prettyprint(ocva.get_element())
    ocva.set_parkingbrake(False,1)
    prettyprint(ocva.get_element())
    ocva.set_steeringwheel(True,1)
    prettyprint(ocva.get_element())
    ocva.set_gear(False,0)
    prettyprint(ocva.get_element())

    ocva1 = OSC.OverrideControllerValueAction()
    ocva1.set_brake(True,2)
    ocva2 = OSC.OverrideControllerValueAction()
    ocva2.set_brake(True,2)
    ocva3 = OSC.OverrideControllerValueAction()
    ocva3.set_brake(True,3)
    assert ocva1 == ocva2
    assert ocva1 != ocva3

def test_visual_action():
    va = OSC.VisibilityAction(True,False,True)
    prettyprint(va.get_element())
    va2 = OSC.VisibilityAction(True,False,True)
    va3 = OSC.VisibilityAction(True,False,False)
    assert va == va2
    assert va != va3

def test_abs_sync_action():
    
    asa = OSC.AbsoluteSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20)
    prettyprint(asa.get_element())
    asa2 = OSC.AbsoluteSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20)
    asa3 = OSC.AbsoluteSynchronizeAction('Ego',OSC.WorldPosition(1,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20)
    assert asa == asa2
    assert asa != asa3

def test_rel_sync_action():
    
    asa = OSC.RelativeSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20,'delta')
    prettyprint(asa.get_element())
    asa2 = OSC.RelativeSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),20,'delta')
    asa3 = OSC.RelativeSynchronizeAction('Ego',OSC.WorldPosition(0,0,0,0,0,0),OSC.WorldPosition(10,0,0,0,0,0),21,'delta')
    assert asa == asa2
    assert asa != asa3

def test_follow_traj_action_polyline():

    positionlist = []
    positionlist.append(OSC.RelativeLanePosition(10,0.5,-3,'Ego'))
    positionlist.append(OSC.RelativeLanePosition(10,1,-3,'Ego'))
    positionlist.append(OSC.RelativeLanePosition(10,-1,-3,'Ego'))
    positionlist.append(OSC.RelativeLanePosition(10,0,-3,'Ego'))
    prettyprint(positionlist[0].get_element())
    polyline = OSC.Polyline([0,0.5,1,1.5],positionlist)


    traj = OSC.Trajectory('my_trajectory',False)
    traj.add_shape(polyline)

    trajact = OSC.FollowTrajectoryAction(traj,OSC.FollowMode.position)
    prettyprint(trajact.get_element())

    trajact2 = OSC.FollowTrajectoryAction(traj,OSC.FollowMode.position)
    traj2 = OSC.Trajectory('my_trajectory',True)
    traj2.add_shape(polyline)

    trajact3 = OSC.FollowTrajectoryAction(traj2,OSC.FollowMode.position)
    assert trajact == trajact2
    assert trajact != trajact3
    

def testParameterAddActions():
    pa = OSC.ParameterAddAction('Myparam',3)
    prettyprint(pa.get_element())
    pa2 = OSC.ParameterAddAction('Myparam',3)
    pa3 = OSC.ParameterAddAction('Myparam',2)
    assert pa == pa2
    assert pa != pa3

def testParameterMultiplyActions():
    pa = OSC.ParameterMultiplyAction('Myparam',3)
    prettyprint(pa)
    pa2 = OSC.ParameterMultiplyAction('Myparam',3)
    pa3 = OSC.ParameterMultiplyAction('Myparam',2)
    assert pa == pa2
    assert pa != pa3


def testParameterSetActions():
    pa = OSC.ParameterSetAction('Myparam',3)
    prettyprint(pa)
    pa2 = OSC.ParameterSetAction('Myparam',3)
    pa3 = OSC.ParameterSetAction('Myparam2',3)
    assert pa == pa2
    assert pa != pa3

def test_trafficsignalstateaction():
    tss = OSC.TrafficSignalStateAction('my signal','red')
    prettyprint(tss)
    tss2 = OSC.TrafficSignalStateAction('my signal','red')
    tss3 = OSC.TrafficSignalStateAction('my signal','green')
    assert tss == tss2
    assert tss != tss3

def test_addEntity():
    ent = OSC.AddEntityAction('my new thingy',OSC.WorldPosition())
    prettyprint(ent)
    ent2 = OSC.AddEntityAction('my new thingy',OSC.WorldPosition())
    ent3 = OSC.AddEntityAction('my new thingy2',OSC.WorldPosition())
    assert ent == ent2
    assert ent != ent3

def test_deleteEntity():
    ent = OSC.DeleteEntityAction('my new thingy')
    prettyprint(ent)
    ent2 = OSC.DeleteEntityAction('my new thingy')
    ent3 = OSC.DeleteEntityAction('my new thingy2')
    assert ent == ent2
    assert ent != ent3

def test_trafficsourceaction():
    
    prop = OSC.Properties()
    prop.add_file('mycontrollerfile.xml')
    controller = OSC.Controller('mycontroller',prop)

    traffic = OSC.TrafficDefinition('my traffic')
    traffic.add_controller(controller,0.5)
    traffic.add_controller(OSC.CatalogReference('ControllerCatalog','my controller'),0.5)

    traffic.add_vehicle(OSC.VehicleCategory.car,0.9)
    traffic.add_vehicle(OSC.VehicleCategory.bicycle,0.1)

    source_action = OSC.TrafficSourceAction(10,10,OSC.WorldPosition(),traffic,100)

    prettyprint(source_action.get_element())

    source_action = OSC.TrafficSourceAction(10,10,OSC.WorldPosition(),traffic)
    prettyprint(source_action.get_element())

    source_action2 = OSC.TrafficSourceAction(10,10,OSC.WorldPosition(),traffic)
    source_action3 = OSC.TrafficSourceAction(10,1,OSC.WorldPosition(),traffic)
    assert source_action == source_action2
    assert source_action != source_action3


def test_trafficsinkaction():
    
    prop = OSC.Properties()
    prop.add_file('mycontrollerfile.xml')
    controller = OSC.Controller('mycontroller',prop)

    traffic = OSC.TrafficDefinition('my traffic')
    traffic.add_controller(controller,0.5)
    traffic.add_controller(OSC.CatalogReference('ControllerCatalog','my controller'),0.5)

    traffic.add_vehicle(OSC.VehicleCategory.car,0.9)
    traffic.add_vehicle(OSC.VehicleCategory.bicycle,0.1)

    sink_action = OSC.TrafficSinkAction(10,10,OSC.WorldPosition(),traffic)
    prettyprint(sink_action.get_element())
    sink_action2 = OSC.TrafficSinkAction(10,10,OSC.WorldPosition(),traffic)
    sink_action3 = OSC.TrafficSinkAction(9,10,OSC.WorldPosition(),traffic)

    assert sink_action == sink_action2
    assert sink_action != sink_action3


    
def test_trafficswarmaction():
    
    prop = OSC.Properties()
    prop.add_file('mycontrollerfile.xml')
    controller = OSC.Controller('mycontroller',prop)

    traffic = OSC.TrafficDefinition('my traffic')
    traffic.add_controller(controller,0.5)
    traffic.add_controller(OSC.CatalogReference('ControllerCatalog','my controller'),0.5)

    traffic.add_vehicle(OSC.VehicleCategory.car,0.9)
    traffic.add_vehicle(OSC.VehicleCategory.bicycle,0.1)

    swarm_action = OSC.TrafficSwarmAction(10,20,10,2,10,'Ego',traffic)
    prettyprint(swarm_action.get_element())

    swarm_action2 = OSC.TrafficSwarmAction(10,20,10,2,10,'Ego',traffic)
    swarm_action3 = OSC.TrafficSwarmAction(10,20,10,2,10,'Ego',traffic,10)
    prettyprint(swarm_action.get_element())

    assert swarm_action == swarm_action2
    assert swarm_action != swarm_action3

def test_environmentaction():
    tod = OSC.TimeOfDay(True,2020,10,1,18,30,30)
    weather = OSC.Weather(OSC.CloudState.free,100,0,1,OSC.PrecipitationType.dry,1)
    rc = OSC.RoadCondition(1)

    env = OSC.Environment(tod,weather,rc)
    ea = OSC.EnvironmentAction('myaction',env)
    prettyprint(ea.get_element())
    ea2 = OSC.EnvironmentAction('myaction',env)
    ea3 = OSC.EnvironmentAction('myaction2',env)
    assert ea == ea2
    assert ea != ea3
