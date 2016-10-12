import os,sys
# This is required because Jenkins doesn't kick of the PVM with a PYTHONPATH set.
sys.path.append('/usr/local/lib/python2.7/site-packages')
import boto3
ec2 = boto3.resource('ec2')
instances = ec2.instances.filter(Filters=[{'Name': 'tag:ShutdownNightly', 'Values': ['true']}])
if None != instances:
    for inst in instances:
        print "Stopping instance {}".format(inst)
        try:
        	inst.stop()
        except Exception as e:
            print "Issue occurred attempting to stop instance {}.\n{}".format(inst,e)