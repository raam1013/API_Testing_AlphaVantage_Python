*** Settings ***
Library  RequestsLibrary

*** Variables ***
${base_url}     https://reqres.in
${page}         2


*** Test Cases ***
Get_emp_Info
    create session mysession    ${base_url}
    ${response}=    get request mysession  /api/users?${page}
    log to console ${response.status_code}
    log to console ${response.content}
    log to console ${response.headers}

