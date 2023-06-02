from django.utils.text import slugify
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

from erp_demo.customer_mng.models import Customer
from erp_demo.dox_mng.models import Document, DocumentLikesToUsers
from erp_demo.hr_mng.models import Employee, Positions, AccessLevels, \
    AccessRights, PositionsToAccessLevels, Trainings, EmployeeToTrainings
from erp_demo.custom_logic import custom_collections
from erp_demo.kpi_mng.models import Kpi
from erp_demo.main_app.models import CaptainsLog, Requirements
from erp_demo.custom_logic.translator import translate_to_maimunica
from erp_demo.opportunity_mng.models import Opportunity
from erp_demo.organization_mng.models import Organization
from erp_demo.process_mng.models import ProcessStepToDocuments, \
    ProcessStep, Process, ProcessToKpis, ProcessToOpportunities, ProcessToRisks
from erp_demo.risk_mng.models import Risk


class DatabaseManipulation:

# Delete whole db (the order is chosen in order not have issues with the links between tables)
# -----------------------------------------------------------------------

    @staticmethod
    def delete_database():
        # M2M tables
        ProcessStepToDocuments.objects.all().delete()
        PositionsToAccessLevels.objects.all().delete()
        EmployeeToTrainings.objects.all().delete()
        DocumentLikesToUsers.objects.all().delete()

        ProcessToKpis.objects.all().delete()
        ProcessToOpportunities.objects.all().delete()
        ProcessToRisks.objects.all().delete()

        # tables with no dependencies to other tables
        AccessLevels.objects.all().delete()
        AccessRights.objects.all().delete()
        Trainings.objects.all().delete()

        # tables with dependencies from other tables
        Positions.objects.all().delete()
        Employee.objects.all().delete()

        ProcessStep.objects.all().delete()
        Document.objects.all().delete()
        Kpi.objects.all().delete()
        Opportunity.objects.all().delete()
        Risk.objects.all().delete()

        Process.objects.all().delete()

        CaptainsLog.objects.all().delete()

        Requirements.objects.all().delete()

        Organization.objects.all().delete()
        Customer.objects.all().delete()

        return 'Successfully deleted'


# Upload to db
# -----------------------------------------------------------------------

    @staticmethod
    def recreate_database(request_object):
        # Select the file
        current_file_path = request_object['select_file']
        workbook = load_workbook(current_file_path)
        worksheet = workbook[workbook.sheetnames[0]]

        # Get the collections
        info_to_update = {}
        list_of_keys = custom_collections.list_of_keys
        coordinates = custom_collections.coordinates

        # Fill the coordinates
        consecutive_empty_rows = 0
        current_row = 1
        current_table = ''
        is_table_header_done = False
        while consecutive_empty_rows < 2:
            row_value = worksheet['A' + str(current_row)].value

            if row_value is None:
                consecutive_empty_rows += 1
                current_row += 1
                is_table_header_done = False
                current_table = ''
                continue

            if current_table == '':
                if row_value in coordinates.keys():
                    current_table = row_value
                    consecutive_empty_rows = 0
                    current_row += 1
                    continue

            if not is_table_header_done:
                current_col = 1
                while 1:
                    col_value = worksheet[get_column_letter(current_col) + str(current_row)].value
                    if col_value is None:
                        is_table_header_done = True
                        current_col -= 1
                        break

                    list_of_keys[current_table].append(col_value)

                    current_col += 1

            if coordinates[current_table]['start_row'] is None:
                coordinates[current_table]['start_row'] = current_row + 1
                coordinates[current_table]['start_column'] = 1
            coordinates[current_table]['end_row'] = current_row
            coordinates[current_table]['end_column'] = current_col
            current_row += 1

        # Update the `info_to_update` with the info from the file
        for table in list_of_keys.keys():

            for row in range(coordinates[table]['start_row'], coordinates[table]['end_row'] + 1):
                # 1 is first row, not 0
                info_to_update[row] = {key: None for key in list_of_keys[table]}

                for col in range(coordinates[table]['start_column'], coordinates[table]['end_column'] + 1):
                    # 1 is first col, not 0
                    char = get_column_letter(col)
                    # == chr(65 + col)
                    info_to_update[row][list_of_keys[table][col-1]] = worksheet[char + str(row)].value

        # Update all table 1 by 1

            if table == 'AccessLevels':
                AccessLevels.objects.bulk_create([AccessLevels(
                    code=info_to_update[obj]['code'],
                    description=info_to_update[obj]['description'],
                ) for obj in info_to_update.keys()])

            elif table == 'AccessRights':
                AccessRights.objects.bulk_create([AccessRights(
                    type=info_to_update[obj]['type'],
                    description=info_to_update[obj]['description'],
                ) for obj in info_to_update.keys()])

            elif table == 'Trainings':
                Trainings.objects.bulk_create([Trainings(
                    code=info_to_update[obj]['code'],
                    name=info_to_update[obj]['name'],
                    description=info_to_update[obj]['description'],
                    # slug=slugify(f"{info_to_update[obj]['code']}"),
                    slug=slugify(f"{info_to_update[obj]['code']}-"
                                 f"{translate_to_maimunica(info_to_update[obj]['name'])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Positions':
                Positions.objects.bulk_create([Positions(
                    code=info_to_update[obj]['code'],
                    name=info_to_update[obj]['name'],
                    access_rights=AccessRights.objects.all()[0],  # ToDo: hardcoded for the excel upload
                ) for obj in info_to_update.keys()])

            elif table == 'Employee':
                Employee.objects.bulk_create([Employee(
                    first_name=info_to_update[row_number]['first_name'],
                    middle_name=info_to_update[row_number]['middle_name'],
                    last_name=info_to_update[row_number]['last_name'],
                    identification=info_to_update[row_number]['identification'],

                    position=Positions.objects.all()[0],  # ToDo: hardcoded for the excel upload

                    contract_number=info_to_update[row_number]['contract_number'],
                    starting_date=info_to_update[row_number]['starting_date'],
                    date_last_hse_training=info_to_update[row_number]['date_last_hse_training'],
                    date_next_hse_training=info_to_update[row_number]['date_next_hse_training'],
                    egn=info_to_update[row_number]['egn'],
                    # slug=slugify(f"{info_to_update[row_number]['first_name']}-{info_to_update[row_number]['last_name']}"),
                    # slug=slugify(f"{info_to_update[row_number]['identification']}-"
                    #              f"{info_to_update[row_number]['position']}"),
                    slug=slugify(f"{info_to_update[row_number]['identification']}-"
                                 f"{translate_to_maimunica(info_to_update[row_number]['first_name'])}-"
                                 f"{translate_to_maimunica(info_to_update[row_number]['last_name'])}"),
                )
                    for row_number in info_to_update.keys()])

            elif table == 'Document':
                Document.objects.bulk_create([Document(
                    type=info_to_update[obj]['type'],
                    number=info_to_update[obj]['number'],
                    name=info_to_update[obj]['name'],
                    revision=info_to_update[obj]['revision'],
                    creation_date=info_to_update[obj]['creation_date'],
                    revision_date=info_to_update[obj]['revision_date'],
                    revision_details=info_to_update[obj]['revision_details'],
                    status=info_to_update[obj]['status'],
                    owner=Employee.objects.all()[0],  # ToDo: hardcoded for the excel upload
                    # slug=slugify(f"{info_to_update[obj]['name']}"),
                    # slug=slugify(f"{info_to_update[obj]['owner']}-"
                    #              f"{info_to_update[obj]['type']}-"
                    #              f"{info_to_update[obj]['revision']}"),
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Process':
                Process.objects.bulk_create([Process(
                    type=info_to_update[obj]['type'],
                    number=info_to_update[obj]['number'],
                    name=info_to_update[obj]['name'],
                    process_owner=Employee.objects.all()[1],  # ToDo: hardcoded for the excel upload 2
                    # slug=slugify(f"{info_to_update[obj]['number']}-"
                    #              f"{info_to_update[obj]['type']}"),
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'ProcessStep':
                ProcessStep.objects.bulk_create([ProcessStep(
                    type=info_to_update[obj]['type'],
                    number=info_to_update[obj]['number'],
                    name=info_to_update[obj]['name'],
                    # parent_process=Process.objects.all()[0],    # ToDo: hardcoded for the excel upload

                    # use the `PXX` from the excel
                    # parent_process=Process.objects.all()[int(info_to_update[obj]['parent_process'][-1])-1],
                    parent_process=Process.objects.all()[int(info_to_update[obj]['parent_process'])-1],

                    description=info_to_update[obj]['description'],
                    responsible=Employee.objects.all()[1],  # ToDo: hardcoded for the excel upload 2
                    # slug=slugify(f"{info_to_update[obj]['name']}"),
                    # slug=slugify(f"{info_to_update[obj]['parent_process']}-"
                    #              f"{info_to_update[obj]['number']}"),
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'][0:50])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Requirements':
                Requirements.objects.bulk_create([Requirements(
                    organization=info_to_update[obj]['organization'],
                    external_document=info_to_update[obj]['external_document'],
                    clause=info_to_update[obj]['clause'],
                    description=info_to_update[obj]['description'],
                    slug=slugify(f"{info_to_update[obj]['organization']}-"
                                 f"{info_to_update[obj]['clause']}-"
                                 f"{translate_to_maimunica(info_to_update[obj]['description'][0:20])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Organization':
                Organization.objects.bulk_create([Organization(
                    name=info_to_update[obj]['name'],
                    eik=info_to_update[obj]['eik'],
                    mol=info_to_update[obj]['mol'],
                    address=info_to_update[obj]['address'],
                    manager_name=info_to_update[obj]['manager_name'],
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'][0:20])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Customer':
                Customer.objects.bulk_create([Customer(
                    type=info_to_update[obj]['type'],
                    name=info_to_update[obj]['name'],
                    registration_address=info_to_update[obj]['registration_address'],
                    registration_city=info_to_update[obj]['registration_city'],
                    eik=info_to_update[obj]['eik'],
                    mol1=info_to_update[obj]['mol1'],
                    mol2=info_to_update[obj]['mol2'],
                    mol3=info_to_update[obj]['mol3'],
                    mol4=info_to_update[obj]['mol4'],
                    mol5=info_to_update[obj]['mol5'],
                    correspondence_address1=info_to_update[obj]['correspondence_address1'],
                    correspondence_address2=info_to_update[obj]['correspondence_address2'],
                    correspondence_address3=info_to_update[obj]['correspondence_address3'],
                    correspondence_address4=info_to_update[obj]['correspondence_address4'],
                    correspondence_address5=info_to_update[obj]['correspondence_address5'],
                    contact_person1=info_to_update[obj]['contact_person1'],
                    contact_person2=info_to_update[obj]['contact_person2'],
                    contact_person3=info_to_update[obj]['contact_person3'],
                    contact_person4=info_to_update[obj]['contact_person4'],
                    contact_person5=info_to_update[obj]['contact_person5'],
                    phone1=info_to_update[obj]['phone1'],
                    phone2=info_to_update[obj]['phone2'],
                    phone3=info_to_update[obj]['phone3'],
                    phone4=info_to_update[obj]['phone4'],
                    phone5=info_to_update[obj]['phone5'],
                    email1=info_to_update[obj]['email1'],
                    email2=info_to_update[obj]['email2'],
                    email3=info_to_update[obj]['email3'],
                    email4=info_to_update[obj]['email4'],
                    email5=info_to_update[obj]['email5'],
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'][0:20])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Kpi':
                Kpi.objects.bulk_create([Kpi(
                    name=info_to_update[obj]['name'],
                    description=info_to_update[obj]['description'],
                    target=info_to_update[obj]['target'],
                    actual_01_23=info_to_update[obj]['actual_01_23'],
                    actual_02_23=info_to_update[obj]['actual_02_23'],
                    actual_03_23=info_to_update[obj]['actual_03_23'],
                    actual_04_23=info_to_update[obj]['actual_04_23'],
                    actual_05_23=info_to_update[obj]['actual_05_23'],
                    actual_06_23=info_to_update[obj]['actual_06_23'],
                    actual_07_23=info_to_update[obj]['actual_07_23'],
                    actual_08_23=info_to_update[obj]['actual_08_23'],
                    actual_09_23=info_to_update[obj]['actual_09_23'],
                    actual_10_23=info_to_update[obj]['actual_10_23'],
                    actual_11_23=info_to_update[obj]['actual_11_23'],
                    actual_12_23=info_to_update[obj]['actual_12_23'],
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'][0:20])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Opportunity':
                Opportunity.objects.bulk_create([Opportunity(
                    name=info_to_update[obj]['name'],
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'][0:20])}"),
                ) for obj in info_to_update.keys()])

            elif table == 'Risk':
                Risk.objects.bulk_create([Risk(
                    name=info_to_update[obj]['name'],
                    slug=slugify(f"{translate_to_maimunica(info_to_update[obj]['name'][0:20])}"),
                ) for obj in info_to_update.keys()])

            info_to_update = {}

        return 'Successfully added \n' \
               '(*documents have no attachments and \n' \
               'process steps have no linked documents!)'
