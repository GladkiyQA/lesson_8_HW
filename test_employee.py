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
    params = {'company': company_id}
    employee_data = api.create_employee_data("Danny", "Test", "testing", "+79991234567", "dan2000@gmail.com", "2000-10-11", "www.path.com", company_id)

    response = api.create_employee(employee_data)
    assert response.status_code == 201
    data = api.get_employee_list(parametres_to_add=params).json()
    assert data[0]['firstName'] == "Danny"
    assert data[0]['lastName'] == "Test"
    assert data[0]['birthdate'] == "2000-10-11"


def test_get_employee_by_id():
    name = 'DannyQA2'
    description = 'blabla2'
    result = api.create_company(name=name, description=description)
    company_id = result['id']

    employee_data = api.create_employee_data("Danny", "Test", "testing", "+79991234567", "dan2000@gmail.com", "2000-10-11", "www.path.com", company_id)

    employee_id = api.create_employee(employee_data).json()['id']

    new_employee = api.get_employee_id(employee_id)
    assert new_employee.status_code == 200

    json_response = new_employee.json()
    assert json_response['firstName'] == "Danny"
    assert json_response['lastName'] == "Test"
    assert json_response['birthdate'] == "2000-10-11"


def test_edit_employee():
    name = 'DannyQA3'
    description = 'blabla3'
    result = api.create_company(name=name, description=description)
    company_id = result['id']
    employee_data = api.create_employee_data("Danny", "Test", "testing", "+79991234567", "dan2000@gmail.com", "2000-10-11", "www.path.com", company_id)
    employee_id = api.create_employee(employee_data).json()['id']

    update_data = api.create_update_data("Новая Фамилия", "новый_email@example.com", "новый_url", "новый_телефон", True)

    response = api.update_employee(employee_id, update_data)
    assert response.status_code == 200
    json_response = api.update_employee(employee_id, update_data).json()
    assert json_response['email'] == "новый_email@example.com"
    assert json_response['url'] == "новый_url"




