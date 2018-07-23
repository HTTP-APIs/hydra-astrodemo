"""
Generated API Documentation for Server API using server_doc_gen.py."""

doc = {
    "@context": {
        "ApiDocumentation": "hydra:ApiDocumentation",
        "description": "hydra:description",
        "domain": {
            "@id": "rdfs:domain",
            "@type": "@id"
        },
        "expects": {
            "@id": "hydra:expects",
            "@type": "@id"
        },
        "hydra": "http://www.w3.org/ns/hydra/core#",
        "label": "rdfs:label",
        "method": "hydra:method",
        "possibleStatus": "hydra:possibleStatus",
        "property": {
            "@id": "hydra:property",
            "@type": "@id"
        },
        "range": {
            "@id": "rdfs:range",
            "@type": "@id"
        },
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "readonly": "hydra:readonly",
        "required": "hydra:required",
        "returns": {
            "@id": "hydra:returns",
            "@type": "@id"
        },
        "statusCode": "hydra:statusCode",
        "statusCodes": "hydra:statusCodes",
        "subClassOf": {
            "@id": "rdfs:subClassOf",
            "@type": "@id"
        },
        "supportedClass": "hydra:supportedClass",
        "supportedOperation": "hydra:supportedOperation",
        "supportedProperty": "hydra:supportedProperty",
        "title": "hydra:title",
        "vocab": "http://astrodemo.com/api/vocab#",
        "writeonly": "hydra:writeonly"
    },
    "@id": "http://astrodemo.com/api/vocab",
    "@type": "ApiDocumentation",
    "description": "AstroDemo",
    "possibleStatus": [],
    "supportedClass": [
        {
            "@id": "vocab:propulsion",
            "@type": "hydra:Class",
            "description": "propulsion",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:propulsion",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Added object successfully",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "Add propulsion object"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Success",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:propulsion",
                    "title": "Add propulsion object"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:power",
                    "readonly": "true",
                    "required": "false",
                    "title": "power",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:mass",
                    "readonly": "true",
                    "required": "false",
                    "title": "mass",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:cost",
                    "readonly": "true",
                    "required": "false",
                    "title": "cost",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:minWorkingTemp",
                    "readonly": "true",
                    "required": "false",
                    "title": "minWorkingTemp",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:maxWorkingTemp",
                    "readonly": "true",
                    "required": "false",
                    "title": "maxWorkingTemp",
                    "writeonly": "true"
                }
            ],
            "title": "propulsion"
        },
        {
            "@id": "vocab:communication",
            "@type": "hydra:Class",
            "description": "communication",
            "supportedOperation": [
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "vocab:communication",
                    "method": "POST",
                    "possibleStatus": [
                        {
                            "description": "Added object successfully",
                            "statusCode": 200
                        }
                    ],
                    "returns": "null",
                    "title": "Creates an existing Spacecraft_Communication entity"
                },
                {
                    "@type": "http://schema.org/UpdateAction",
                    "expects": "null",
                    "method": "GET",
                    "possibleStatus": [
                        {
                            "description": "Success",
                            "statusCode": 200
                        }
                    ],
                    "returns": "vocab:communication",
                    "title": "Add propulsion object"
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:power",
                    "readonly": "true",
                    "required": "false",
                    "title": "power",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:mass",
                    "readonly": "true",
                    "required": "false",
                    "title": "mass",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:cost",
                    "readonly": "true",
                    "required": "false",
                    "title": "cost",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:minWorkingTemp",
                    "readonly": "true",
                    "required": "false",
                    "title": "minWorkingTemp",
                    "writeonly": "true"
                },
                {
                    "@type": "SupportedProperty",
                    "property": "vocab:maxWorkingTemp",
                    "readonly": "true",
                    "required": "false",
                    "title": "maxWorkingTemp",
                    "writeonly": "true"
                }
            ],
            "title": "communication"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Collection",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "null",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "Collection"
        },
        {
            "@id": "http://www.w3.org/ns/hydra/core#Resource",
            "@type": "hydra:Class",
            "description": "null",
            "supportedOperation": [],
            "supportedProperty": [],
            "title": "Resource"
        },
        {
            "@id": "vocab:propulsionCollection",
            "@type": "hydra:Class",
            "description": "A collection of propulsion",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:propulsion_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all propulsion entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:propulsionCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:propulsion_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new propulsion entitity",
                    "expects": "vocab:propulsion",
                    "method": "PUT",
                    "returns": "vocab:propulsion",
                    "statusCodes": [
                        {
                            "description": "If the propulsion entity was created successfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The propulsion",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "propulsionCollection"
        },
        {
            "@id": "vocab:communicationCollection",
            "@type": "hydra:Class",
            "description": "A collection of communication",
            "subClassOf": "http://www.w3.org/ns/hydra/core#Collection",
            "supportedOperation": [
                {
                    "@id": "_:communication_collection_retrieve",
                    "@type": "http://schema.org/FindAction",
                    "description": "Retrieves all communication entities",
                    "expects": "null",
                    "method": "GET",
                    "returns": "vocab:communicationCollection",
                    "statusCodes": []
                },
                {
                    "@id": "_:communication_create",
                    "@type": "http://schema.org/AddAction",
                    "description": "Create new communication entitity",
                    "expects": "vocab:communication",
                    "method": "PUT",
                    "returns": "vocab:communication",
                    "statusCodes": [
                        {
                            "description": "If the communication entity was created successfully.",
                            "statusCode": 201
                        }
                    ]
                }
            ],
            "supportedProperty": [
                {
                    "@type": "SupportedProperty",
                    "description": "The communication",
                    "property": "http://www.w3.org/ns/hydra/core#member",
                    "readonly": "false",
                    "required": "false",
                    "title": "members",
                    "writeonly": "false"
                }
            ],
            "title": "communicationCollection"
        },
        {
            "@id": "vocab:EntryPoint",
            "@type": "hydra:Class",
            "description": "The main entry point or homepage of the API.",
            "supportedOperation": [
                {
                    "@id": "_:entry_point",
                    "@type": "http://schema.org/FindAction",
                    "description": "The APIs main entry point.",
                    "expects": "null",
                    "method": "GET",
                    "returns": "null",
                    "statusCodes": "vocab:EntryPoint"
                }
            ],
            "supportedProperty": [
                {
                    "hydra:description": "The propulsionCollection collection",
                    "hydra:title": "propulsioncollection",
                    "property": {
                        "@id": "vocab:EntryPoint/propulsion",
                        "@type": "hydra:Link",
                        "description": "The propulsionCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "propulsionCollection",
                        "range": "vocab:propulsionCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:propulsion_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all propulsion entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:propulsionCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:propulsion_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new propulsion entitity",
                                "expects": "vocab:propulsion",
                                "method": "PUT",
                                "returns": "vocab:propulsion",
                                "statusCodes": [
                                    {
                                        "description": "If the propulsion entity was created successfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                },
                {
                    "hydra:description": "The communicationCollection collection",
                    "hydra:title": "communicationcollection",
                    "property": {
                        "@id": "vocab:EntryPoint/communication",
                        "@type": "hydra:Link",
                        "description": "The communicationCollection collection",
                        "domain": "vocab:EntryPoint",
                        "label": "communicationCollection",
                        "range": "vocab:communicationCollection",
                        "supportedOperation": [
                            {
                                "@id": "_:communication_collection_retrieve",
                                "@type": "http://schema.org/FindAction",
                                "description": "Retrieves all communication entities",
                                "expects": "null",
                                "method": "GET",
                                "returns": "vocab:communicationCollection",
                                "statusCodes": []
                            },
                            {
                                "@id": "_:communication_create",
                                "@type": "http://schema.org/AddAction",
                                "description": "Create new communication entitity",
                                "expects": "vocab:communication",
                                "method": "PUT",
                                "returns": "vocab:communication",
                                "statusCodes": [
                                    {
                                        "description": "If the communication entity was created successfully.",
                                        "statusCode": 201
                                    }
                                ]
                            }
                        ]
                    },
                    "readonly": "true",
                    "required": "null",
                    "writeonly": "false"
                }
            ],
            "title": "EntryPoint"
        }
    ],
    "title": "AstroDemo"
}