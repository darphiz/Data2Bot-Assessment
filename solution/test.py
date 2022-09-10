import unittest

from main import load_json, get_proper_schema_type_name, generate_schema, write_json

class TestSchemaUtilsFunctions(unittest.TestCase):
    
    
    def test_json_load(self):
        """Test if the JSON file is loaded correctly"""
        
        data = load_json('./tests/input/0.json')
        no_data = load_json('./tests/input/8.json')
        bad_data = load_json('./tests/input/1.json')
        
        self.assertEqual(data, {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(no_data, None)
        self.assertEqual(bad_data, {})

    def test_can_get_proper_schema_type_name(self):
        """
            Test if the proper schema type name is returned
            By default, python returns a short name for the type
            which is not compatible with JSON schema
        """
        
        schema_name = get_proper_schema_type_name('str')
        invalid_schema_name = get_proper_schema_type_name('invalid')
        self.assertEqual(schema_name, 'string')
        self.assertEqual(invalid_schema_name, 'invalid')


    def test_can_generate_schema(self):
        
        """Test if the schema is generated correctly"""
        data = load_json('./tests/input/0.json')
        invalid_data = load_json('./tests/input/1.json')
        schema = generate_schema(data)
        generate_invalid_schema = generate_schema(invalid_data)
        self.assertEqual(schema, {
                                        "a": {
                                            "type": "integer",
                                            "tag": "",
                                            "description": "",
                                            "required": False
                                        },
                                        "b": {
                                            "type": "integer",
                                            "tag": "",
                                            "description": "",
                                            "required": False
                                        },
                                        "c": {
                                            "type": "integer",
                                            "tag": "",
                                            "description": "",
                                            "required": False
                                        }
                                    }
                         
                         )
        self.assertEqual(generate_invalid_schema, {})
    
    
    def test_can_write_json(self):
        
        """Test if the JSON file is written correctly"""
        data = load_json('./tests/input/0.json')
        schema = generate_schema(data)
        write_json(schema, 'test')
        self.assertEqual(load_json('./data/output/test.json'), schema)


    def test_can_read_and_generate_schema(self):
        """Test if the schema is generated correctly from a JSON file"""
        
        file_name = '0'
        data = load_json(f'./tests/input/{file_name}.json')
        schema = generate_schema(data)
        write_json(schema, file_name)
        self.assertEqual(load_json(f'./data/output/{file_name}.json'), schema)


if __name__ == '__main__':
    unittest.main()