from django.contrib.sites.models import Site
from .models import Account, Image
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


class BasicImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'image_small')

    def validate_image(self, value):
        """
        Check that image extension is .jpg or .png.
        """
        image = str(value).split('.')
        extension = image[-1]
        if (extension != 'jpg') and (extension != 'png'):
            raise serializers.ValidationError("The image is not .jpg or .png format.")
        return value

    image_small = serializers.SerializerMethodField()

    def get_image_small(self, obj):
        """
        Return address url to image thumbnail.
        """
        acconut = Account.objects.get(name='Basic')
        size = f"{acconut.size_small}x{acconut.size_small}"
        return Site.objects.get_current().domain + get_thumbnail(obj.image, size).url

    def to_representation(self, instance):
        """
        Prepare data to display.
        """
        data = super(BasicImageSerializer, self).to_representation(instance)
        return {
            'image_small' : data['image_small']
        }


class PremiumImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'image_small', 'image_large', 'image_original')

    image_small = serializers.SerializerMethodField()
    image_large = serializers.SerializerMethodField()
    image_original = serializers.SerializerMethodField('get_image_original')

    def validate_image(self, value):
        """
        Check that image extension is .jpg or .png.
        """
        image = str(value).split('.')
        extension = image[-1]
        if (extension != 'jpg') and (extension != 'png'):
            raise serializers.ValidationError("Image is not .jpg or .png format.")
        return value

    def get_image_small(self, obj):
        """
        Return address url to image thumbnail.
        """
        acconut = Account.objects.get(name='Premium')
        size = f"{acconut.size_small}x{acconut.size_small}"
        return Site.objects.get_current().domain + get_thumbnail(obj.image, size).url

    def get_image_large(self, obj):
        """
        Return address url to image thumbnail.
        """
        acconut = Account.objects.get(name='Premium')
        size = f"{acconut.size_large}x{acconut.size_large}"
        return Site.objects.get_current().domain + get_thumbnail(obj.image, size).url

    def get_image_original(self, obj):
        """
        Return address url to original image.
        """
        return Site.objects.get_current().domain + obj.image.url

    def to_representation(self, instance):
        """
        Prepare data to display.
        """
        data = super(PremiumImageSerializer, self).to_representation(instance)
        return {
                'image_small' : data['image_small'],
                'image_large' : data['image_large'],
                'image_original' : data['image_original'],
            }


class EnterpriseImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'image_small', 'image_large', 'image_original')

    image_small = serializers.SerializerMethodField()
    image_large = serializers.SerializerMethodField()
    image_original = serializers.SerializerMethodField('get_image_original')

    def validate_image(self, value):
        """
        Check that image extension is .jpg or .png.
        """
        image = str(value).split('.')
        extension = image[-1]
        if (extension != 'jpg') and (extension != 'png'):
            raise serializers.ValidationError("Image is not .jpg or .png format.")
        return value

    def get_image_small(self, obj):
        """
        Return address url to image thumbnail.
        """
        acconut = Account.objects.get(name='Premium')
        size = f"{acconut.size_small}x{acconut.size_small}"
        return Site.objects.get_current().domain + get_thumbnail(obj.image, size).url

    def get_image_large(self, obj):
        """
        Return address url to image thumbnail.
        """
        acconut = Account.objects.get(name='Premium')
        size = f"{acconut.size_large}x{acconut.size_large}"
        return Site.objects.get_current().domain + get_thumbnail(obj.image, size).url

    def get_image_original(self, obj):
        """
        Return address url to original image.
        """
        return Site.objects.get_current().domain + obj.image.url

    def to_representation(self, instance):
        """
        Prepare data to display.
        """
        data = super(EnterpriseImageSerializer, self).to_representation(instance)
        return {
                'image_small' : data['image_small'],
                'image_large' : data['image_large'],
                'image_original' : data['image_original'],
            }
