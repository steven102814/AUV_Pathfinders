import rospy
from kellerLD import KellerLD
from std_msgs.msg import Float32

def sensor_node():
    rospy.init_node('keller_ld_sensor_node', anonymous=True)
    pub_pressure = rospy.Publisher('keller_ld/pressure', Float32, queue_size=10)
    pub_temperature = rospy.Publisher('keller_ld/temperature', Float32, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    sensor = KellerLD()
    if not sensor.init():
        rospy.logerr("Failed to initialize Keller LD sensor!")
        return

    while not rospy.is_shutdown():
        try:
            sensor.read()
            pressure = sensor.pressure()
            temperature = sensor.temperature()
            rospy.loginfo("Pressure: %7.4f bar, Temperature: %0.2f C" % (pressure, temperature))
            pub_pressure.publish(pressure)
            pub_temperature.publish(temperature)
        except Exception as e:
            rospy.logerr(e)
        rate.sleep()

if __name__ == '__main__':
    try:
        sensor_node()
    except rospy.ROSInterruptException:
        pass
