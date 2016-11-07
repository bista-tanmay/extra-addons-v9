from openerp import models, fields, api, _

class calculate(models.TransientModel):
	_name='calculate.calculate'

	num1=fields.Float("Enter Num 1")
	num2=fields.Float("Enter Num 2")
	select=fields.Selection({('addition','Sum'),('subtraction','Minus')})

	@api.multi
	def calculate(self):
		temp=0
		if self.select == "addition":
			temp=self.num1+self.num2
		else:
			temp=self.num1-self.num2
		context=dict(self._context)
		context.update({'default_result':temp})

		return{
			'name': _('Calculate'),
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'calculate.result',
			'target': 'new',
			'context': context
			}

class result(models.TransientModel):
	_name='calculate.result'

	result=fields.Float("Result")