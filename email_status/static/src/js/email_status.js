openerp.email_status = function (session) {
    var _t = session.web._t,
       _lt = session.web._lt;

    var mail = session.mail;


        mail.ThreadMessage.include({
            init: function (parent, datasets, options) {
            this._super(parent, datasets, options);

            this.state = datasets.state || false;
        },
});
};
