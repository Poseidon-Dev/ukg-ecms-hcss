resp = """
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope" xmlns:a="http://www.w3.org/2005/08/addressing">
    <s:Header>
        <a:Action s:mustUnderstand="1">http://www.ultipro.com/services/employeeperson/IEmployeePerson/FindPeopleResponse</a:Action>
    </s:Header>
    <s:Body>
        <FindPeopleResponse xmlns="http://www.ultipro.com/services/employeeperson">
            <FindPeopleResult xmlns:b="http://www.ultipro.com/contracts" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
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
                    <b:PagingInfo>
                        <b:CurrentPage>1</b:CurrentPage>
                        <b:PageSize>100</b:PageSize>
                        <b:PageTotal>1</b:PageTotal>
                        <b:TotalItems>3</b:TotalItems>
                    </b:PagingInfo>
                    <b:RequestNumber i:nil="true"/>
                    <b:Success>true</b:Success>
                </b:OperationResult>
                <b:Results>
                    <b:EmployeePerson>
                        <b:CompanyCode>APC</b:CompanyCode>
                        <b:EmployeeNumber>12799</b:EmployeeNumber>
                        <b:FirstName>Johnny</b:FirstName>
                        <b:LastName>Whitworth</b:LastName>
                        <b:People>
                            <b:Person>
                                <b:AlternateEmailAddress i:nil="true"/>
                                <b:EmailAddress i:nil="true"/>
                                <b:EmployeeIdentifier i:type="b:EmployeeNumberIdentifier">
                                    <b:CompanyCode>APC</b:CompanyCode>
                                    <b:EmployeeNumber>12799</b:EmployeeNumber>
                                </b:EmployeeIdentifier>
                                <b:FirstName>Johnny</b:FirstName>
                                <b:FormerLastName i:nil="true"/>
                                <b:LastName>Whitworth</b:LastName>
                                <b:MiddleName>Mac Thomas</b:MiddleName>
                                <b:PreferredFirstName i:nil="true"/>
                                <b:Prefix i:nil="true"/>
                                <b:SSN>607664199</b:SSN>
                                <b:SelfServiceProperties i:nil="true" xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
                                <b:Suffix i:nil="true"/>
                                <b:SuppressSSN>true</b:SuppressSSN>
                            </b:Person>
                        </b:People>
                    </b:EmployeePerson>
                    <b:EmployeePerson>
                        <b:CompanyCode>APC</b:CompanyCode>
                        <b:EmployeeNumber>16719</b:EmployeeNumber>
                        <b:FirstName>Johnny</b:FirstName>
                        <b:LastName>Medel</b:LastName>
                        <b:People>
                            <b:Person>
                                <b:AlternateEmailAddress i:nil="true"/>
                                <b:EmailAddress i:nil="true"/>
                                <b:EmployeeIdentifier i:type="b:EmployeeNumberIdentifier">
                                    <b:CompanyCode>APC</b:CompanyCode>
                                    <b:EmployeeNumber>16719</b:EmployeeNumber>
                                </b:EmployeeIdentifier>
                                <b:FirstName>Johnny</b:FirstName>
                                <b:FormerLastName i:nil="true"/>
                                <b:LastName>Medel</b:LastName>
                                <b:MiddleName>Anthony</b:MiddleName>
                                <b:PreferredFirstName i:nil="true"/>
                                <b:Prefix i:nil="true"/>
                                <b:SSN>551656164</b:SSN>
                                <b:SelfServiceProperties i:nil="true" xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
                                <b:Suffix i:nil="true"/>
                                <b:SuppressSSN>true</b:SuppressSSN>
                            </b:Person>
                        </b:People>
                    </b:EmployeePerson>
                    <b:EmployeePerson>
                        <b:CompanyCode>APC</b:CompanyCode>
                        <b:EmployeeNumber>17493</b:EmployeeNumber>
                        <b:FirstName>Johnny</b:FirstName>
                        <b:LastName>Gutierrez</b:LastName>
                        <b:People>
                            <b:Person>
                                <b:AlternateEmailAddress i:nil="true"/>
                                <b:EmailAddress i:nil="true"/>
                                <b:EmployeeIdentifier i:type="b:EmployeeNumberIdentifier">
                                    <b:CompanyCode>APC</b:CompanyCode>
                                    <b:EmployeeNumber>17493</b:EmployeeNumber>
                                </b:EmployeeIdentifier>
                                <b:FirstName>Johnny</b:FirstName>
                                <b:FormerLastName i:nil="true"/>
                                <b:LastName>Gutierrez</b:LastName>
                                <b:MiddleName>Angelo</b:MiddleName>
                                <b:PreferredFirstName i:nil="true"/>
                                <b:Prefix i:nil="true"/>
                                <b:SSN>680100779</b:SSN>
                                <b:SelfServiceProperties i:nil="true" xmlns:c="http://schemas.microsoft.com/2003/10/Serialization/Arrays"/>
                                <b:Suffix i:nil="true"/>
                                <b:SuppressSSN>true</b:SuppressSSN>
                            </b:Person>
                        </b:People>
                    </b:EmployeePerson>
                </b:Results>
            </FindPeopleResult>
        </FindPeopleResponse>
    </s:Body>
</s:Envelope>
"""