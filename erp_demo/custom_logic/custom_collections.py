document_types_en = (
    ('All', 'All'),
    ('External', 'External'),
    ('Policy', 'Policy'),
    ('Manual', 'Manual'),
    ('Procedure', 'Procedure'),
    ('Instruction', 'Instruction'),
    ('Form', 'Form'),
)

document_types_bg = (
    ('All', 'Всички'),
    ('External', 'External'),
    ('Policy', 'Policy'),
    ('Manual', 'Ръководство'),
    ('Procedure', 'Процедура'),
    ('Instruction', 'Инструкция'),
    ('Form', 'Формуляр'),
)

search_types_en = {
    ('All', 'All'),
    ('Process', 'Processes'),
    ('ProcessStep', 'Process steps'),
    ('Document', 'Documents'),
    ('Employee', 'Employees'),
    ('Trainings', 'Trainings'),
    ('Organization', 'Organization'),
    ('Customer', 'Customer'),
    ('Interaction', 'Interaction'),
    ('Risk', 'Risk'),
    ('Opportunity', 'Opportunity'),
    ('Kpi', 'Kpi'),
    ('Resource', 'Resource'),
    ('Requirements', 'Requirements'),
    ('Nonconformity', 'Nonconformity'),
}

search_types_bg = {
    ('All', 'Всички'),
    ('Process', 'Процеси'),
    ('ProcessStep', 'Процесни стъпки'),
    ('Document', 'Документи'),
    ('Employee', 'Служители'),
    ('Trainings', 'Обучения'),
    ('Organization', 'Организации'),
    ('Customer', 'Клиенти'),
    ('Interaction', 'Взаимодействия'),
    ('Risk', 'Рискове'),
    ('Opportunity', 'Възможности'),
    ('Kpi', 'Kpi'),
    ('Resource', 'Ресурси'),
    ('Requirements', 'Изисквания'),
    ('Nonconformity', 'Несъответствия'),
}

process_numbers = (
    ('All', 'All'),
    ('P01', 'P01'),
    ('P02', 'P02'),
    ('P03', 'P03'),
    ('P04', 'P04'),
    ('P05', 'P05'),
    ('P06', 'P06'),
    ('P07', 'P07'),
    ('P08', 'P08'),
    ('P09', 'P09'),
    ('P10', 'P10'),
    ('P11', 'P11'),
    ('P12', 'P12'),
    ('P13', 'P13'),
    ('P14', 'P14'),
    ('P15', 'P15'),
    ('P16', 'P16'),
    ('P17', 'P17'),
    ('P18', 'P18'),
    ('P20', 'P20'),
    ('P21', 'P21'),
    ('P22', 'P22'),
    ('P23', 'P23'),
    ('P24', 'P24'),
    ('P25', 'P25'),
)

list_of_keys = {
    'AccessLevels': [],
    'AccessRights': [],
    'Positions': [],
    'Trainings': [],
    'Employee': [],
    'Document': [],
    'Process': [],
    'ProcessStep': [],
    'Requirements': [],
    'Organization': [],
    'Customer': [],
    'Kpi': [],
    'Opportunity': [],
    'Risk': [],
    'Interaction': [],
    'Resource': [],
    'Nonconformity': [],
}

coordinates = {
    'AccessLevels': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'AccessRights': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Positions': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Trainings': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Employee': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Document': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Process': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'ProcessStep': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Requirements': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Organization': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Customer': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Kpi': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Opportunity': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Risk': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Interaction': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Resource': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
    'Nonconformity': {
        'start_row': None,
        'end_row': None,
        'start_column': None,
        'end_column': None,
    },
}

logging_info_stack = []

cyrillic_chars = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
    'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'ю', 'я',
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й',
    'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
    'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'ь', 'Ю', 'Я',
]

corresponding_english_chars = [
    'a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y',
    'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
    'f', 'h', 'ts', 'ch', 'sh', 'sht', 'a', 'a', 'yu', 'ya',
    'A', 'B', 'V', 'G', 'D', 'E', 'Zh', 'Z', 'I', 'Y',
    'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U',
    'F', 'H', 'Ts', 'Ch', 'Sh', 'Sht', 'A', 'a', 'Yu', 'Ya',
]
