def perform_operation(num1, num2, operation):
	match operation:
		case  'add':
			return (num1 + num2)
		case 'subtract':
			return (num1 - num2)
		case 'multiply':
			return (num1 * num2)
		case 'divide':
			if num2:
				return (num1 / num2)
			else:
				print("Non zero division")


