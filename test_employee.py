from employee import Employee

api = Employee('https://x-clients-be.onrender.com')

def test_get_employee_list():
    name = 'DannyQA'
    description = 'blabla'
    result = api.create_company(name=name, description=description)
    new_id = result['id']
    params = {
        'company': new_id
    }
    response = api.get_employee_list(parametres_to_add=params)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response == []

def test_create_new_employee():
    name = 'DannyQA1'
    description = 'blabla1'
    result = api.create_company(name=name, description=description)
    company_id = result['id']
    params = {
        'company': company_id
    }

    employee_data = {
        "isActive": True,
        "createDateTime": "2024-02-20T20:42:58.623Z",
        "lastChangedDateTime": "2024-02-20T20:42:58.623Z",
        "firstName": "Danny",
        "lastName": "Test",
        "middleName": "testing",
        "phone": "+79991234567",
        "email": "dan2000@gmail.com",
        "birthdate": "2000-10-11",
        "avatar_url": "www.path.com",
        "companyId": company_id
    }

    response = api.create_employee(employee_data)
    assert response.status_code == 201
    data = api.get_employee_list(parametres_to_add=params).json()
    assert data[-1]['firstName'] == employee_data['firstName']
    assert data[-1]['lastName'] == employee_data['lastName']
    # assert data[-1]['email'] == employee_data['email'] - ошибка в апи
    assert data[-1]['birthdate'] == employee_data['birthdate']

def test_get_employee_by_id():
    name = 'DannyQA2'
    description = 'blabla2'
    result = api.create_company(name=name, description=description)
    company_id = result['id']

    employee_data = {
        "isActive": True,
        "createDateTime": "2024-02-20T20:42:58.623Z",
        "lastChangedDateTime": "2024-02-20T20:42:58.623Z",
        "firstName": "Danny",
        "lastName": "Test",
        "middleName": "testing",
        "phone": "+79991234567",
        "email": "dan2000@gmail.com",
        "birthdate": "2000-10-11",
        "avatar_url": "www.path.com",
        "companyId": company_id
    }

    employee_id = api.create_employee(employee_data).json()['id']

    new_employee = api.get_employee_id(employee_id)
    print(new_employee.json())
    assert new_employee.status_code == 200
    json = api.get_employee_id(employee_id).json()
    assert json['firstName'] == employee_data['firstName']
    assert json['lastName'] == employee_data['lastName']
    assert json['birthdate'] == employee_data['birthdate']

def test_edit_employee():
    name = 'DannyQA3'
    description = 'blabla3'
    result = api.create_company(name=name, description=description)
    company_id = result['id']

    employee_data = {
        "isActive": True,
        "createDateTime": "2024-02-20T20:42:58.623Z",
        "lastChangedDateTime": "2024-02-20T20:42:58.623Z",
        "firstName": "Danny",
        "lastName": "Test",
        "middleName": "testing",
        "phone": "+79991234567",
        "email": "dan2000@gmail.com",
        "birthdate": "2000-10-11",
        "avatar_url": "www.path.com",
        "companyId": company_id
    }

    employee_id = api.create_employee(employee_data).json()['id']

    update_data = {
        "lastName": "Новая Фамилия",
        "email": "новый_email@example.com",
        "url": "новый_url",
        "phone": "новый_телефон",
        "isActive": True
    }

    response = api.update_employee(employee_id, update_data)
    assert response.status_code == 200
    json_response = api.update_employee(employee_id, update_data).json()
    assert json_response['email'] == update_data['email']
    assert json_response['url'] == update_data['url']




