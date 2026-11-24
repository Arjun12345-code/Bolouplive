<?php

$coinlye_theme_data = wp_get_theme();

/*
 * Define theme version
 */
define('COINLYE_VERSION', (WP_DEBUG) ? time() : $coinlye_theme_data->get('Version'));

/*
 * Inc folder directory
 */
define('COINLYE_INC_DIR', get_template_directory() . '/inc/');

/*
 * After setup theme
 */
require_once COINLYE_INC_DIR . 'theme-setup.php';

/*
 * Load default theme options
 */
 require_once COINLYE_INC_DIR . 'cs-framework-functions.php';

/*
 * Load meta box and theme options if Codestar framework installed.
 */
if( class_exists( 'CSF' ) ) {
    // require_once COINLYE_INC_DIR . 'metabox-and-options/metabox-and-options.php';
}

/**
 * Template Functions
 */
require COINLYE_INC_DIR . 'template-functions.php';

/*
 * Enqueue styles and scripts.
 */
require_once COINLYE_INC_DIR . 'css-and-js.php';

/*
 * Register widget area
 */
require_once COINLYE_INC_DIR . 'widget-area-init.php';

/**
 * tgmp functions file
 */
require_once COINLYE_INC_DIR . 'class-tgm-plugin-activation.php';
require_once COINLYE_INC_DIR . 'add-plugin.php';

/*
 * Load inline style.
 */
require_once COINLYE_INC_DIR . 'inline-style.php';

/**
 * Implement the Custom Header feature.
 */
require COINLYE_INC_DIR . 'custom-header.php';

/**
 * Custom template tags for this theme.
 */
require COINLYE_INC_DIR . 'class-wp-coinlye-navwalker.php';

/**
 * coinlye Core Functions
 */
require COINLYE_INC_DIR . 'coinlye-helper-class.php';

/**
 * Customizer additions.
 */
require COINLYE_INC_DIR . '/customizer.php';

/**
 * Load Jetpack compatibility file.
 */
if ( defined( 'JETPACK__VERSION' ) ) {
    require COINLYE_INC_DIR . '/jetpack.php';
}

/*
 * Comment Template
 */
require_once COINLYE_INC_DIR . 'comment-template.php';

/*
 * Import Demo Content
 */
require_once COINLYE_INC_DIR . 'demo-content/import-demo-content.php';