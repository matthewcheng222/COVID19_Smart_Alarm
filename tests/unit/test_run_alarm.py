import run_alarm

def test_run_alarm_alarmnomatch(): #Alarm label passed not in list -> No alarm created
    run_alarm.run_alarm("Hello World")
    assert len(run_alarm.alarm_list_sched) == 0

def test_run_alarms_normal():
    to_append = {'alarm_label':"Hello World",
    'time_delay_sec':10,
    'announcement_type':"announcement_default",
    'id_key':"alarm_Hello_World_for_time"}
    run_alarm.alarm_list_sched.append(to_append)
    run_alarm.run_alarm("Hello World")
    for alarms in run_alarm.alarm_list_sched:
        assert alarms['alarm_label'] == "Hello World"

def test_run_alarm_notstring():
    run_alarm.alarm_list_sched = []
    run_alarm.run_alarm(10)
    assert len(run_alarm.alarm_list_sched) == 0
    