odoo.define('home_background_image.Home', function (require) {
"use strict";

var session = require('web.session');
var HomeMenu = require('web_enterprise.HomeMenu');

/*
 * Notice:
 *  some features (like seeing the home menu background) are available
 *  even the user is not a system user, this is why there are two different
 *  includes in Studio for this module.
 */

HomeMenu.include({
    /**
     * @override
     */
    start: function () {
        this._setBackgroundImage();
        return this._super.apply(this, arguments);
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * Put the home menu background as the cover of current `$el`.
     *
     * @private
     */
    _setBackgroundImage: function () {
        var url = session.url('/web/image', {
            model: 'res.company',
            id: session.user_context.allowed_company_ids[0],
            field: 'background_image',
        });
        this.$el.css({
            "background-image": "url(" + url + ")",
            "background-size": "cover",
        });
    },
});

});
