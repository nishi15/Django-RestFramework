from rest_framework import serializers

from myApiView import models



class CustomerSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    print('CustomerSerializer\n')

    class Meta:
        model = models.CustomerModel
        fields = ('id', 'email', 'full_name', 'password','customer_address')
        extra_kwargs = {
            "password": {
                "style": {
                    "input_type": "password",
                },
                "write_only": True,
            }
        }

    def create(self, validated_data):
        """create and return new user"""
        user = models.CustomerModel.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            # date_joined =validated_data['date_joined'],
            customer_address = validated_data['customer_address']
        )

        print("serializer validated data " + str(validated_data))

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        instance.email = validated_data.get('email', instance.email)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.customer_address = validated_data.get('customer_address', instance.customer_address)

        instance.save()
        return instance

        # return super().update(instance, validated_data)


