import logging
import sched
import time
from announcement import announcement

alarms_list = []
alarm_list_sched = []

s = sched.scheduler(time.time, time.sleep)

def run_alarm(alarm_label : str):
    """
    Adding the created alarm into the scheduler.

    The function takes input alarm_label and reads the information about
    the alarm from the list alarm_list_sched, which consist of name of
    alarm, time difference between now and the alarm, type of announcement
    to be announced, and the time of creation of the alarm. The function
    then add the alarm into the schedulerusing the sched module.

    Keyword Arguments:
        alarm_label -- The name of the alarm to be added to the scheduler
    """
    for alarms in alarm_list_sched:
        if alarms['alarm_label'] == alarm_label:
            #Creating alarm if alarm_label match
            priority = alarm_list_sched.index(alarms) + 1
            #Alarms created latter have lower priority
            alarm_label = alarms['alarm_label']
            time_delay = alarms['time_delay_sec']
            announcement_type = alarms['announcement_type']
            alarms['id_key'] = s.enter(time_delay, priority, announcement,\
                kwargs={'alarm_label' : alarm_label,\
                    'announcement_type' : announcement_type})
            #Using id_key as unique identifier for alarm
            logging.info(s.queue) #Logging queue of schedule