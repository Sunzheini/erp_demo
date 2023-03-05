from django.core.exceptions import ValidationError


def validate_file_size(file):
    filesize = file.file.size
    limit_in_mb = 10.0
    if filesize > limit_in_mb * 1024 * 1024:
        raise ValidationError(f"Max file size is {limit_in_mb}")
