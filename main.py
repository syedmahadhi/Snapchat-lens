from robolink import* #api 
from robodk import* #math toolbox


RL = Robolink()#start the api
robot = RL.Item('KUKA KR 6 R900 sixx',ITEM_TYPE_ROBOT)#get robot

home = RL.Item('Home')
#get refrence target by name
target = RL.Item('Target 1')#target for welding
target_i = TL.Item('Target 2')#target for painting
poseref = target.Pose()

#move to refrence point
robot.MoveJ(home)
robot.MoveJ(target)

#draw a hexagon around the target
for i in range(7):
  ang = i*2pi/6
  posei = poseref*rotz(ang)*transl(200,0,0)*rotz(-ang)
  robot.MoveL(posei)#move to new target
  
  
robot.MoveL(target)#move back to refrence target
robot.MoveJ(target_i)#move to painting target

#draw a hexagon around the target
for i in range(7):
  ang = i*2pi/6
  posep = poseref*rotz(ang)*transl(200,0,0)*rotz(-ang)
  robot.MoveL(posep)#move to new target

robot.MoveL(target_i)#move to refrence target
robot.MoveJ(home)#back to initial position
