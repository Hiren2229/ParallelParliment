from rami.models import MembersData


def create_records_with_additional_fields(model_cls, records_data_list):
    created_ids = []

    for record_data in records_data_list:
        # Add the additional fields 'field1' and 'field2' to the record_data dictionary
        record_data['field1'] = 'some_value'
        record_data['field2'] = 'another_value'

        # Create a new instance of the model with the provided data
        new_record = model_cls(**record_data)

        # Save the instance to the database
        new_record.save()

        # Append the created ID to the list
        created_ids.append(new_record.id)

    return created_ids