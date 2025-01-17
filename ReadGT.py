import rosbag
import rospy

# get gt from output_bag
bag_filepath = "/home/zeng/vmono/indoor_forward_3_davis_with_gt.bag"
bag = rosbag.Bag(bag_filepath)
output_filepath = "groundturth9.txt"

# groundtruth_odom_topic = "/groundtruth/odometry"
groundtruth_pose_topic = "/groundtruth/pose"
data_topics = ["/groundtruth/pose"]

# store the info in the corresponding list
# groundtruth_odom_list = []
groundtruth_pose_list = []

for topic,msg,t in bag.read_messages(topics = data_topics):
if (topic == groundtruth_pose_topic):
# timestamp = round(msg.header.stamp, 9)
timestamp = msg.header.stamp.secs
timestamp = int(str(timestamp)[:10])
seq = msg.header.seq
tx = msg.pose.position.x
ty = msg.pose.position.y
tz = msg.pose.position.z
qx = msg.pose.orientation.x
qy = msg.pose.orientation.y
qz = msg.pose.orientation.z
qw = msg.pose.orientation.w
groundtruth_pose_list.append([timestamp,tx, ty, tz, qx, qy, qz, qw])

with open(output_filepath, "w") as file_pose:
for array in groundtruth_pose_list:
line = ' '.join(map(str, array)) + "\n"
file_pose.write(line)

print("groundtruth has been extracted and saved")
