from cores.base_module import Scanner


class Check(Scanner):
    def signature(self):
        # Signature by github.com/dmknght
        return {
            "MySQL Injection": [
                "You have an error in your SQL syntax",
                "supplied argument is not a valid MySQL",
                "mysql_fetch_array() expects parameter 1 to be resource, boolean given in"
            ],
            "Java SQL Injection": [
                "java.sql.SQLException: Syntax error or access violation",
                "java.sql.SQLException: Unexpected end of command"
            ],
            "PostgreSQL Injection": [
                "PostgreSQL query failed: ERROR: parser:",
            ],
            "XPathException": [
                "XPathException",
                "Warning: SimpleXMLElement::xpath():"
            ],
            "MSSQL Injection": [
                "[Microsoft][ODBC SQL Server Driver]",
                "Microsoft OLE DB Provider for ODBC Drivers</font> <font size=\"2\" face=\"Arial\">error",
                "Microsoft OLE DB Provider for ODBC Drivers",
            ],
            "MSAccess SQL Injection": [
                "[Microsoft][ODBC Microsoft Access Driver]",
            ],
            "LDAP Injection": [
                "supplied argument is not a valid ldap",
                "javax.naming.NameNotFoundException"
            ],
            "DB2 Injection": [
                "DB2 SQL error:"
            ],
            "Interbase Injection": [
                "Dynamic SQL Error",
            ],
            "Sybase Injection": [
                "Sybase message:",
            ],
            ".NET SQL Injection": [
                "Unclosed quotation mark after the character string",
            ],
        }

    def gen_payload(self):
        pass

