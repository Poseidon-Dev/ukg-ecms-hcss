resp = """
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing">
    <s:Header>
        <a:Action s:mustUnderstand="1">http://www.ultipro.com/services/employeeperson/IEmployeePerson/GetPersonByEmployeeIdentifierResponse</a:Action>
    </s:Header>
    <s:Body>
        <GetPersonByEmployeeIdentifierResponse xmlns="http://www.ultipro.com/services/employeeperson">
            <GetPersonByEmployeeIdentifierResult xmlns:b="http://www.ultipro.com/contracts" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
                <b:OperationResult>
                    <b:HasErrors>false</b:HasErrors>
                    <b:HasWarnings>false</b:HasWarnings>
                    <b:Messages>
                        <b:OperationMessage>
                            <b:Code>OK</b:Code>
                            <b:LogEntryId i:nil="true"/>
                            <b:Message>OK</b:Message>
                            <b:PropertyName i:nil="true"/>
                            <b:Severity>Information</b:Severity>
                        </b:OperationMessage>
                    </b:Messages>
                    <b:PagingInfo i:nil="true"/>
                    <b:RequestNumber i:nil="true"/>
                    <b:Success>true</b:Success>
                </b:OperationResult>
                <b:Results>
                    <b:Person>
                        <b:AlternateEmailAddress i:nil="true"/>
                        <b:EmailAddress>testemployee@arizonapipeline.com</b:EmailAddress>
                        <b:EmployeeIdentifier i:type="b:EmployeeNumberIdentifier">
                            <b:CompanyCode>APC</b:CompanyCode>
                            <b:EmployeeNumber>99998</b:EmployeeNumber>
                        </b:EmployeeIdentifier>
                        <b:FirstName>Employee</b:FirstName>
                        <b:FormerLastName i:nil="true"/>
                        <b:LastName>TestAPIP</b:LastName>
                        <b:MiddleName i:nil="true"/>
                        <b:PreferredFirstName>Employee</b:PreferredFirstName>
                        <b:Prefix i:nil="true"/>
                        <b:SSN>999999997</b:SSN>
                        <b:SelfServiceProperties i:nil="true" xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
                        <b:Suffix i:nil="true"/>
                        <b:SuppressSSN>false</b:SuppressSSN>
                    </b:Person>
                </b:Results>
            </GetPersonByEmployeeIdentifierResult>
        </GetPersonByEmployeeIdentifierResponse>
    </s:Body>
</s:Envelope>
"""