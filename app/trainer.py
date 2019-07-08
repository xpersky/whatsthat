def trainer():

    from keras.preprocessing.image import ImageDataGenerator
    from keras.optimizers import RMSprop
    from keras.models import load_model
    import tensorflow as tf
    import os
    
    graph = tf.get_default_graph()
    model = load_model(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'whatsthat.h5'))

    batch_size = 32

    images_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'media/images') 

    train_datagen = ImageDataGenerator(rescale=1./255,
                                    rotation_range=40,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True,
                                    vertical_flip=True,
                                    fill_mode='nearest',
                                    validation_split=0.3)

    train_gen = train_datagen.flow_from_directory(images_path,batch_size=batch_size,subset='training')
    valid_gen = train_datagen.flow_from_directory(images_path,batch_size=batch_size,subset='validation')

    with graph.as_default():
        
        model.compile(optimizer=RMSprop(lr=1e-5),
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

        model.fit_generator(train_gen,
                            epochs=10,
                            steps_per_epoch = len(train_gen) // batch_size,
                            validation_data = valid_gen,
                            validation_steps = len(valid_gen) // batch_size)

        model.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'whatsthat.h5'))
