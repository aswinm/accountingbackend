from rest_framework import serializers
from projects.models import Project, TimeDuration

import datetime

class ProjectSerializer(serializers.ModelSerializer):
        time_durations = serializers.StringRelatedField(many=True,read_only=True)
        class Meta:
                    model = Project
                    fields = ('id','name','client','total_cost','total_duration','time_durations')

class TimeDurationSerializer(serializers.ModelSerializer):
        class Meta:
                    model = TimeDuration
                    fields = ('id','from_time','to_time','project','duration')

        def create(self, validated_data):
                    time_duration = TimeDuration.objects.create(**validated_data)
                    time_duration.from_time = datetime.datetime.strptime(time_duration.from_time, "%Y-%m-%d %H:%M:%S")
                    time_duration.to_time = datetime.datetime.strptime(time_duration.to_time, "%Y-%m-%d %H:%M:%S")
                    duration = time_duration.to_time - time_duration.from_time            
                    time_duration.project.total_duration_num += int(duration.total_seconds())
                    time_duration.project.set_duration_string()
                    time_duration.duration = str(duration)
                    time_duration.save()
                    return time_duration

