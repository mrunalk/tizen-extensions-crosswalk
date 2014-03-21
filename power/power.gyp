{
  'includes':[
    '../common/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'tizen_power',
      'type': 'loadable_module',
      'sources': [
        'power_api.js',
        'power_extension.cc',
        'power_extension.h',
        'power_instance_desktop.cc',
        'power_instance_desktop.h',
        'power_types.h',
        '../common/extension.h',
        '../common/extension.cc',
      ],
      'includes': [
        '../common/pkg-config.gypi',
      ],
      'conditions': [
        ['tizen == 1', {
          'variables': {
            'packages': [
              'glib-2.0',
              'capi-system-device',
              'capi-system-power',
              'pmapi',
              'vconf',
            ]
          },
          'sources': [
            'power_event_source.cc',
            'power_event_source.h',
            'power_instance.cc',
            'power_instance.h',
          ],
        }],
        ['extension_host_os == "desktop"', {
          'variables': {
            'packages': [
              'gio-2.0',
            ]
          },
        }],
      ],
    },
  ],
}
