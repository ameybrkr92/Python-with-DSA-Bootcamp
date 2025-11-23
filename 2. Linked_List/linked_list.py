head = {
       "value":24,
       "next":  {
            "value":2,
            "next": {
                "value":4,
                "next": {
                    "value":24,
                    "next":None
                        }
                     }
                }
        }

print(head['next'],"\n")
print(head["next"]["value"],"\n")
print(head["next"]["next"],"\n")
print(head["next"]["next"]["next"]["next"],"\n")
