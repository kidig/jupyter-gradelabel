define([
    'require',
    'jquery',
    'base/js/namespace',
    'base/js/events',
], function (
    requirejs,
    $,
    Jupiter,
    events
) {
    "use strict";

    function setup_gradelabel() {
        console.log('setup gradelabel');
    }

    function load_extension() {
        if (Jupiter.notebook.kernel) {
            setup_gradelabel();
        } else {
            events.on('kernel_ready.Kernel', setup_gradelabel);
        }
    }

    return {
        load_ipython_extension: load_extension,
    }
});