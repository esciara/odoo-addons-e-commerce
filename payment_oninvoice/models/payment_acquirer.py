# -*- coding: utf-8 -*-

from openerp.addons.payment.models.payment_acquirer import ValidationError
from openerp.osv import osv
from openerp.tools.float_utils import float_compare
from openerp.tools.translate import _

import logging
import pprint

_logger = logging.getLogger(__name__)


class OnInvoicePaymentAcquirer(osv.Model):
    _inherit = 'payment.acquirer'

    def _get_providers(self, cr, uid, context=None):
        providers = super(OnInvoicePaymentAcquirer, self)._get_providers(cr, uid, context=context)
        providers.append(['oninvoice', _('Payment on Invoice')])
        return providers

    def oninvoice_get_form_action_url(self, cr, uid, id, context=None):
        return '/payment/oninvoice/feedback'


class OnInvoicePaymentTransaction(osv.Model):
    _inherit = 'payment.transaction'

    def _oninvoice_form_get_tx_from_data(self, cr, uid, data, context=None):
        reference, amount, currency_name = data.get('reference'), data.get('amount'), data.get('currency_name')
        tx_ids = self.search(
                cr, uid, [
                    ('reference', '=', reference),
                ], context=context)

        if not tx_ids or len(tx_ids) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx_ids:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return self.browse(cr, uid, tx_ids[0], context=context)

    def _oninvoice_form_get_invalid_parameters(self, cr, uid, tx, data, context=None):
        invalid_parameters = []

        if float_compare(float(data.get('amount', '0.0')), tx.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % tx.amount))
        if data.get('currency') != tx.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), tx.currency_id.name))

        return invalid_parameters

    def _oninvoice_form_validate(self, cr, uid, tx, data, context=None):
        _logger.info('Validated on invoice payment for tx %s: set as pending' % (tx.reference))
        return tx.write({'state': 'pending'})
