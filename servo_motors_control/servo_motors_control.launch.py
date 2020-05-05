import launch
import launch_ros.actions

def generate_launch_description():

    ### ここにlaunchしたいノードを定義
    ### node_executableのところは、setup.pyのなかの
    ### entry_pointsで指定した （例）pub = node.Pub:main
    ### の左辺側の文字と合わせて下さい
    servo_control = launch_ros.actions.Node(
        package='servo_motors_control', node_executable='servo_control', output='screen')
    key_control = launch_ros.actions.Node(
        package='servo_motors_control', node_executable='key_control', output='screen')

    ### こちらにもlaunchしたいノードを記述
    ### 上記で定義した （例）pub = launch_ros.actions.Node
    ### の、左辺側の変数を列挙します。
    ### 記述しなかったら、そのノードは起動しません。
    ###
    ### target_action=sub に記述したノードが落ちたら、
    ### launchで起動したものが一式落ちます。
    return launch.LaunchDescription([
        servo_control,
        key_control,
        # TODO(wjwwood): replace this with a `required=True|False` option on ExecuteProcess().
        # Shutdown launch when client exits.
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=key_control,
                on_exit=[launch.actions.EmitEvent(
                    event=launch.events.Shutdown())],
            )),
    ])