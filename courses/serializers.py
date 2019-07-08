from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('address', 'latitude', 'longitude', 'course')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value', 'course')


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category', 'logo', 'contacts', 'branches']

    def create(self, validated_data):
        if 'branches' in validated_data:
            branches_data = validated_data.pop('branches')
        if 'contacts' in validated_data:
            contacts_data = validated_data.pop('contacts')
        course = Course.objects.create(**validated_data)
        branches_list = []
        contacts_list = []
        print(contacts_data)
        print(branches_data)
        for branches_details in branches_data:
            branches_list.append(Branch.objects.create(
                course_id=course.id,
                **branches_details))
        for contacts_details in contacts_data:
            contacts_list.append(Contact.objects.create(
                course_id=course.id,
                **contacts_details))
        course.save()
        return course
